=====================================
Documentation
=====================================


MulticomponentMatcher
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pyhamcrest_toolbox.multicomponent.MulticomponentMatcher

The class that is the base for writing multicomponent matchers, i.e. the
ones that have the form of::

    assert_that(someting, matches_someting(x).and_something_else(y))

In your subclass, all you **have** to do is write your ``and_something_else()``
methods that register your matcher plugins. **NOTE** that you have to
return ``self`` from such methods, as (a) that is required for chaining, and (b)
the final instance returned by the chain must be a matcher.

You can write your main matching logic in the traditional way, but you can
also register a matcher plugin from your ``__init__`` method.

The MatcherPlugin entities are still matchers and can be used outside of
MulticomponentMatchers. They can be reused in several MulticomponentMatchers,
or they can even be grouped into mixins and plugged in as bunches.

Here's an example of what a subclass of the ``MulticomponentMatcher`` could
look like:

.. code-block:: python

    class GrailMatcher(MulticomponentMatcher):
        def __init__(self, is_holy):
            self.register(GrailHolynessMatcher(is_holy))

        def with_width(width):
            self.register(GrailWidthMatcher(wrap_matcher(width)))
            return self

        def with_height(height):
            self.register(GrailHeightMatcher(wrap_matcher(height)))
            return self

And this is all it takes to write your multicomponent matcher. All the descriptions
and mismatch descriptions will be build automatically from the plugins.

register
^^^^^^^^

.. automethod:: pyhamcrest_toolbox.multicomponent.MulticomponentMatcher.register


MatcherPlugin
^^^^^^^^^^^^^^^^^^

.. autoclass:: pyhamcrest_toolbox.multicomponent.MatcherPlugin

This is the class to extend when you create your matcher plugins for a
multicomponent matcher. Instead of overriding the usual ``BaseMatcher``
methods, you need to override the ones below.

The original standard ``BaseMatcher`` methods are replaced with these ones because
they are overridden in the ``MatcherPlugin`` class to work with the
``MulticomponentMatcher``.


component_matches
^^^^^^^^^^^^^^^^^

.. automethod:: pyhamcrest_toolbox.multicomponent.MatcherPlugin.component_matches

Return ``True`` if it matches, ``False`` otherwise.

describe_to
^^^^^^^^^^^^^^

.. automethod:: pyhamcrest_toolbox.multicomponent.MatcherPlugin.describe_to

The same as ``desribe_to`` in ``Matcher``
(:py:meth:`hamcrest.core.selfdescribing.SelfDescribing.describe_to`). Add the
description of the object you expect to the description provided.

describe_component_mismatch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: pyhamcrest_toolbox.multicomponent.MatcherPlugin.describe_component_mismatch

Basically, the same as :py:meth:`hamcrest.core.matcher.Matcher.describe_mismatch`.

Here is an example of what a ``GrailHolynessMatcher`` might look like:
