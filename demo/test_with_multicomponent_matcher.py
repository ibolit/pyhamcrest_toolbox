import pytest
from hamcrest import assert_that, greater_than, anything, less_than
from hamcrest.core.helpers.wrap_matcher import wrap_matcher

from demo.grail import Grail
from pyhamcrest_toolbox.multicomponent import (
    MatcherPlugin,
    MulticomponentMatcher
)
from pyhamcrest_toolbox.wrapper_base import MatcherPluginWrapper


class HolinessMatcher(MatcherPlugin):
    def __init__(self, holy=True):
        super().__init__()
        self.holy = holy

    def component_matches(self, item):
        return item.holy == self.holy

    def describe_to(self, description):
        description.append_text(
            'a grail that is {}holy'.format('' if self.holy else 'not '))

    def describe_component_mismatch(self, item, mismatch_description):
        mismatch_description.append('the grail was {}holy'.format(
            '' if item.holy else 'not '))


class DimensionsMatcher(MatcherPluginWrapper):
    def __init__(self, dimension):
        super().__init__(anything())
        self.matcher = wrap_matcher(dimension)


class WidthMatcher(DimensionsMatcher):
    description_prefix = 'with width '
    mismatch_description_prefix = 'the width '

    def convert_item(self, item):
        return item.width


class GrailMatcher(MulticomponentMatcher):
    def is_holy(self, holy=True):
        return self.register(HolinessMatcher(holy))

    def with_width(self, width):
        return self.register(WidthMatcher(width))


def grail():
    return GrailMatcher()


@pytest.fixture
def my_grail():
    return Grail(height=2, width=3, depth=4)


class TestGrail:
    def test_holiness(self, my_grail):
        assert_that(my_grail, grail().is_holy())

    def test_width(self, my_grail):
        assert_that(my_grail, grail().with_width(greater_than(4)))

    def test_width_and_holiness(self, my_grail):
        assert_that(
            my_grail,
            grail()
                .is_holy()
                .with_width(greater_than(4)))

    def test_correct_width_wrong_holiness(self, my_grail):
        assert_that(
            my_grail,
            grail()
                .is_holy()
                .with_width(less_than(4)))
