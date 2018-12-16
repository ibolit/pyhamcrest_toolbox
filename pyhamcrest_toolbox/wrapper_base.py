from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.isequal import IsEqual

from pyhamcrest_toolbox.multicomponent import MatcherPlugin


class MatcherPluginWrapper(MatcherPlugin):
    """This class allows turning good old matchers into matcher plugins
    that can be used in MulticomponentMatchers.
    """
    matcher_class = IsEqual
    """Set this variable to the class of the matcher you want to wrap. 
    If you don't, it IsEqual will be used (which is returned by the `equal_to`)
    function. Note, that you have to specify a class, not a function."""
    description_prefix = ""
    """The prefix that will be added to the description of the wrapped
    matcher"""
    mismatch_description_prefix = ""
    """The prefix to be added to the mismatch_description"""


    def convert_item(self, item):
        """Convert the item that the MulticomponentMatcher deals with into
        the item that your component plugin is responsible for.

        The multicomponent matcher will pass the item that it has received, and
        it is up to your matcher plugin to get the object that it works with
        from that object. By default, returns the item itself.
        """
        return item


    def __init__(self, *args, **kwargs):
        if not issubclass(self.matcher_class, BaseMatcher):
            raise RuntimeError(
                "type_ must be set and must inherit from BaseMatcher")

        super().__init__()
        self.matcher = self.matcher_class(*args, **kwargs)


    def component_matches(self, item):
        return self.matcher._matches(self.convert_item(item))


    def describe_to(self, description):
        description\
            .append_text(self.description_prefix)
        self.matcher.describe_to(description)


    def describe_component_mismatch(self, item, mismatch_description):
        mismatch_description.append_text(self.mismatch_description_prefix)
        self.matcher.describe_mismatch(
            self.convert_item(item), mismatch_description)
