from hamcrest.core.base_matcher import BaseMatcher

from .util import get_description, get_mismatch_description, sentence_case


class MatcherPlugin(BaseMatcher):
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


class MulticomponentMatcher(BaseMatcher):
    def __init__(self, *args, **kwargs):
        self._matchers = {}


    def _matches(self, item):
        match_result = True
        for m in self._matchers:
            r = m._matches(item)
            self._matchers[m] = r
            match_result &= r

        return match_result


    def register(self, plugin):
        """
        Call this method to register your plugins to your matcher, either from
        your additional matcher methods (``with_something`` or ``and_someting``)
        or from the ``__init__`` method. **NOTE** that you **must** return ``self``
        from those additional matcher methods.

        :param plugin: Instances of ``MatcherPluginMixin``
        :return:
        """
        self._matchers[plugin] = False
        return self


    def describe_to(self, description):
        descriptions = [
            get_description(m)
            for m in self._matchers]
        a = "{}.".format("; ".join(descriptions))
        a = sentence_case(a)
        description.append_text(a)


    def describe_mismatch(self, item, mismatch_description):
        m_desrs = [
            get_mismatch_description(m, item)
            for m, result in self._matchers.items()
            if not result]
        m_desrs = filter(None, m_desrs)
        a = sentence_case("{}.".format("; ".join(m_desrs)))
        mismatch_description.append_text(a)


class KwargMulticomponentMatcher(MulticomponentMatcher):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def register_for_kwarg(self, plugin, kwarg=None):
        """Register a plugin for a plugin for a kwarg argument"""
        if kwarg is not None:
            self.register(plugin)
