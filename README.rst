.. image:: https://api.codeclimate.com/v1/badges/511fa5e42116a9ab746b/maintainability
   :target: https://codeclimate.com/github/ibolit/pyhamcrest_toolbox/maintainability
   :alt: Maintainability

======================
PyHamcrest Toolbox
======================

PyHamcrest is a great thing for writing reusable tests, but sometimes
writing your own matchers may be a bit of a chore. This project aims at
making this task easy, fast and even fun (for want of a better word).

To reiterate the obvious, a test should always do all the checks it has to do,
and even if some of them fail, the rest should still be run. That way you will
get a better idea of what's gone wrong with your code, and you will waste
less time fixing the first of the checks only to find the the second one is
still failing, and that means that you should have fixed the first one in a
different way.

So, instead of this:

.. code:: python

    def test_the_holy_grail():
        the_holy_grail = seek_the_holy_grail()
        assert_that(the_holy_grail.is_holy(), is_(True))
        assert_that(the_holy_grail.depth, greater_than(5))
        assert_that(the_holy_grail.width, greater_than(6))
        assert_that(the_holy_grail.height, greater_than(7))

this should be written:

.. code:: python

    def test_the_holy_grail():
        the_holy_grail = seek_the_holy_grail()
        assert_that(
            the_holy_grail,
            is_holy()\
                .with_depth(greater_than(5)).\
                .with_width(greater_than(6)).\
                .with_height(greater_than(7))
        )

The second one, however, requires writing your own matchers. With this toolbox,
it is easy.

All you have to do is to write your ``is_holy`` matcher that inherits from the
``MultisegmentMatcher`` as the backbone. Then you write individual matchers
for each of the holy grail properties enhancing them with the
``MatcherPluginMixin``, and you register them with the ``is_holy`` matcher.

So, this is your ``is_holy`` matcher:

.. code:: python

    class IsHolyMatcher(MultisegmentMatcher):
        def __init__(self):
            super().__init__()

    def is_holy():
        return IsHolyMatcher()

And that's it. You don't have to override the usual matcher methods. Everything
will be done by the parent class. However, it doesn't do any matching yet, so we
need to write the plugins. Let's start with the actual holyness:

.. code:: python

    class HolynessMatcher(BaseMatcher, MatcherPluginMixin):
        def __init__(is_holy=True):
            super().__init__()
            self.is_holy = is_holy

        def component_matches(self, item):
            # the item will be a grail
            return self.is_holy == item.is_holy()

        def describe_to(self, description):
            description.append_text(
                "A grail which is {}holy".format("" if self.is_holy else "not "))

        def describe_component_mismatch(self, item, mismatch_description):
            mismatch_description.append_text(
                "The grail was {}holy".format("" if item.is_holy() else "not "))

And then you register it with the main matcher:

.. code:: python

    class IsHolyMatcher(MultisegmentMatcher):
        def __init__(self, is_holy):
            super().__init__()
            self.register(HolynessMatcher(is_holy))

    def holy(is_holy):
        return IsHolyMatcher(is_holy)

Of course, you could write that ``HolynessMatcher`` logic in your
``IsHolyMatcher``, but if we have the power of plugins, then why not use it?

For now, we only have this bit: ``assert_that(the_grail, is_holy())``, and
not the ``.with_width(...)`` stuff. So let's write it. I won't go through the
process of writing the plugin for the width as it is rather straightforward,
but here's how you register it with the main matcher:

.. code:: python

    class IsHolyMatcher(MultisegmentMatcher):
        def __init__(self, is_holy):
            super().__init__()
            self.register(HolynessMatcher(is_holy))

        def with_width(self, value):
            self.register(GrailWidthMatcher(value))
            return self

    def holy(is_holy):
        return IsHolyMatcher(is_holy)

Now you can do the ``is_holy().with_width(greater_than(5))`` stuff.
**Note that you have to return** ``self`` **from the plugin registering methods**,
as (a) you might want to chain them, and (b) the result of the chain still
needs to be a matcher.
