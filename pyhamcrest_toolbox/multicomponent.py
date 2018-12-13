from hamcrest.core.base_matcher import BaseMatcher

from .util import get_mismatch_description


class MatcherPluginMixin:
    def __init__(self, *args, **kwargs):
        self.passed = False


    def _matches(self, item):
        self.passed = self.component_matches(item)
        return self.passed


    def component_matches(self, item):
        raise NotImplementedError()


    def describe_mismatch(self, item, mismatch_description):
        if not self.passed:
            self.describe_component_mismatch(item, mismatch_description)


    def describe_component_mismatch(self, item, mismatch_description):
        raise NotImplementedError()


class MultisegmentMatcher(BaseMatcher):
    """Makes use of the MatcherPluginMixin.
    The idea is that you register component matchers that
    do the comparison of the actual parts of the thing that should be
    verified by this matcher. You just add methods like `with_headers()`,
    which add the matcher to self.matchers. Don't forget to return `self`.

    """
    def __init__(self, *args, **kwargs):
        self._matchers = []


    def _matches(self, item):
        match_result = True
        for m in self._matchers:
            match_result &= m._matches(item)

        return match_result


    def register(self, plugin):
        self._matchers.append(plugin)


    def describe_to(self, description):
        for m in self._matchers:
            description.append_description_of(m)


    def describe_mismatch(self, item, mismatch_description):
        m_desrs = [get_mismatch_description(m, item) for m in self._matchers]
        m_desrs = filter(None, m_desrs)
        mismatch_description.append_text("; ".join(m_desrs))
