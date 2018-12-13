from hamcrest.core.string_description import StringDescription


def get_mismatch_description(matcher, item):
    descr = StringDescription()
    matcher.describe_mismatch(item, descr)
    return str(descr)


# def get_description(matcher):
#     descr = StringDescription()
#     matcher.describe_to(descr)
#     return str(descr)

def add_not_to_str(a_str, add_not):
    return "{}{}".format(
            "" if add_not else "not ", a_str)
