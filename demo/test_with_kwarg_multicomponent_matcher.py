import pytest
from hamcrest import assert_that, greater_than, less_than

from demo.grail import Grail
from demo.test_with_multicomponent_matcher import HolinessMatcher, WidthMatcher
from pyhamcrest_toolbox.multicomponent import KwargMulticomponentMatcher


class GrailMatcher(KwargMulticomponentMatcher):
    def __init__(self, holy=None, width=None):
        super().__init__()
        self.register_for_kwarg(HolinessMatcher(holy), holy)
        self.register_for_kwarg(WidthMatcher(width), width)


def grail(holy=None, width=None):
    return GrailMatcher(holy, width)


@pytest.fixture
def my_grail():
    return Grail(height=2, width=3, depth=4)


class TestGrail:
    def test_holiness(self, my_grail):
        assert_that(my_grail, grail(holy=True))

    def test_width(self, my_grail):
        assert_that(my_grail, grail(width=greater_than(4)))

    def test_width_and_holiness(self, my_grail):
        assert_that(
            my_grail,
            grail(holy=True, width=greater_than(4)))

    def test_correct_width_wrong_holiness(self, my_grail):
        assert_that(
            my_grail,
            grail(holy=True, width=less_than(4)))
