import pytest
from hamcrest import assert_that
from hamcrest.core.core.isequal import IsEqual
from pyhamcrest_metamatchers.metamatchers import doesnt_match, matches

from pyhamcrest_toolbox.multicomponent import (
    KwargMulticomponentMatcher
)
from pyhamcrest_toolbox.wrappers import InstanceOfPlugin


class MyNumber:
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other

    def __repr__(self):
        return "Value: {}".format(self.n)


class MatcherForTest(KwargMulticomponentMatcher):
    def __init__(self, number, type_=None):
        super().__init__()
        self.register(IsEqual(number))
        self.register_for_kwarg(InstanceOfPlugin(type_), type_)


def my_number(n, type_=None):
    return MatcherForTest(n, type_)


class TestKwargMulticomponentMatcher:
    def test_with_a_kwarg(self):
        assert_that(
            my_number(4, type_=MyNumber),
            matches(MyNumber(4))
                .with_description(
                '<4>; an instance of MyNumber.'))


    def test_with_a_wrong_type(self):
        assert_that(
            my_number(4, type_=int),
            doesnt_match(MyNumber(4))
                .with_mismatch_description(
                    "The type was "
                    "<class 'tests.test_kwarg_multicomponent_matcher.MyNumber'>."))


    def test_with_wrong_number(self):
        assert_that(
            my_number(5, type_=MyNumber),
            doesnt_match(MyNumber(4))
                .with_mismatch_description('Was <Value: 4>.'))


    @pytest.mark.parametrize('number', [
        MyNumber(4), 4, 4.0
    ])
    def test_with_no_kwarg(self, number):
        assert_that(
            my_number(4),
            matches(number)
        )

