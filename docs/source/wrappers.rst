===============
Wrappers
===============

In order to get going with the toolbox easily, it is important to be able to
use your existing matchers with it. To that end, we have created a wrapper
that turns your existing matchers to plugins.

MatcherPluginWrapper
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pyhamcrest_toolbox.wrapper_base.MatcherPluginWrapper

matcher_class
^^^^^^^^^^^^^

.. autoattribute:: pyhamcrest_toolbox.wrapper_base.MatcherPluginWrapper.matcher_class

description_prefix
^^^^^^^^^^^^^^^^^^

.. autoattribute:: pyhamcrest_toolbox.wrapper_base.MatcherPluginWrapper.description_prefix

mismatch_description_prefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoattribute:: pyhamcrest_toolbox.wrapper_base.MatcherPluginWrapper.mismatch_description_prefix

convert_item
^^^^^^^^^^^^

.. automethod:: pyhamcrest_toolbox.wrapper_base.MatcherPluginWrapper.convert_item
