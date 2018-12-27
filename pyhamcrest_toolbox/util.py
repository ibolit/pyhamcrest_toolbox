from hamcrest.core.string_description import StringDescription


def get_mismatch_description(matcher, item):
    """Get the mismatch description of a matcher with a particular item.

    :param matcher:
    :type matcher: BaseMatcher
    :param item:
    :type item: Any
    :return: The string representation of the mismatch description
    :rtype: str
    """
    descr = StringDescription()
    matcher.describe_mismatch(item, descr)
    return str(descr)


def get_description(matcher):
    """Get the string representation of a matcher's description
    """
    descr = StringDescription()
    matcher.describe_to(descr)
    return str(descr)


def add_not_to_str(a_str, not_):
    """
    Prefix a string with a not depending on the bool parameter
    >>> add_not_to_str("hello", True)  # "hello"
    >>> add_not_to_str("hello", False)  # "not hello"

    :param a_str:
    :type a_str:
    :param add_not:
    :type not_:
    :return:
    :rtype:
    """
    return "{}{}".format(
            "" if not_ else "not ", a_str)


def sentence_case(string):
    """
    Capitalize the first letter of the string. Does not capitalize after
    full stops and other sentence dividing punctuation.

    :param string: a string to capitalize
    :type string: str
    :return:
    :rtype: str
    """
    return "{}{}".format(string[0].capitalize(), string[1:])
