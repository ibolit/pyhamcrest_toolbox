from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.string_description import StringDescription


class CumulativeDescriptionMatcher(BaseMatcher):
    def __init__(self, expected):
        super().__init__()
        self.expected = expected
        self.mismatch_description = StringDescription()
        self.result = True
        self.description = StringDescription()
        self.test_object = None


    def check_with_description(self, item_name, matcher):
        item = self.test_object.get(item_name)
        result = matcher.matches(item)
        self.result &= result

        expected = StringDescription()
        matcher.describe_to(expected)
        self.description.append_text("<{}: {}>;".format(item_name, expected))

        if not result:
            actual = StringDescription()
            matcher.describe_mismatch(item, actual)
            self.mismatch_description.append_text(
                "\n\t{}: Expected: {}, but was {}".format(
                    item_name, expected, actual
                )
            )


    def _matches(self, item):
        self.test_object = item
        for field, matcher in self.field_matchers_dict().items():
            self.check_with_description(
                field, matcher
            )
        return self.result


    def field_matchers_dict(self):
        raise NotImplementedError(
            "Provide a dictionary of fields in the actual dict and matchers that should match their values"
        )


    def describe_to(self, description):
        description.append_text(self.description)


    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text(self.mismatch_description)
