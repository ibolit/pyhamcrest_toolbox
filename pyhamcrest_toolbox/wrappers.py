from hamcrest.core.core.isanything import IsAnything
from hamcrest.core.core.isinstanceof import IsInstanceOf

from pyhamcrest_toolbox.wrapper_base import MatcherPluginWrapper


class InstanceOfPlugin(MatcherPluginWrapper):
    matcher_class = IsInstanceOf

    def describe_component_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('the type was {}'.format(type(item)))


class IsAnythingPlugin(MatcherPluginWrapper):
    matcher_class = IsAnything


