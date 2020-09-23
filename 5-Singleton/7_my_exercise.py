"""Nothing to comment"""


def is_singleton(factory):
    """todo: call factory() and return true or false depending on whether the
    makes a singleton or not"""
    my_obj = factory()
    my_obj2 = factory()
    return my_obj is my_obj2
