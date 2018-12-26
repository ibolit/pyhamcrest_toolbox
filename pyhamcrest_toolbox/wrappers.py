from hamcrest.core.core.isanything import IsAnything
from hamcrest.core.core.isinstanceof import IsInstanceOf

from pyhamcrest_toolbox.wrapper_base import MatcherPluginWrapper


class InstanceOfPlugin(MatcherPluginWrapper):
    matcher_class = IsInstanceOf


class IsAnythingPlugin(MatcherPluginWrapper):
    matcher_class = IsAnything


