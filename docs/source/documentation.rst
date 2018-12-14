=====================================
Documentation
=====================================


MultisegmentMatcher
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pyhamcrest_toolbox.multicomponent.MultisegmentMatcher

The class that is the base for writing multicomponent matchers, i.e. the
ones that have the form of::

    assert_that(someting, matches_someting(x).and_something_else(y))

In your subclass, all you **have** to do is write your ``and_something_else()``
methods that register your matcher plugins. **NOTE** that you have to
return ``self`` from such methods, as (a) that is required for chaining, and (b)
the final instance returned by the chain must be a matcher.

You can write your main matching logic in the traditional way, but you can
also register a matcher plugin from your ``__init__`` method.

Here's an example of what a subclass of the ``MultisegmentMatcher`` could
look like:

.. code-block:: python

    class GrailMatcher(MultisegmentMatcher):
        def __init__(self, is_holy):
            self.register(GrailHolynessMatcher(is_holy))

        def with_width(width):
            self.register(GrailWidthMatcher(wrap_matcher(width)))
            return self

         def with_height(height):
             self.register(GrailHeightMatcher(wrap_matcher(height)))
             return self

And this is all it takes to write your multisegment matcher. All the descriptions
and mismatch descriptions will be build automatically from the plugins.

register
^^^^^^^^

.. automethod:: pyhamcrest_toolbox.multicomponent.MultisegmentMatcher.register
