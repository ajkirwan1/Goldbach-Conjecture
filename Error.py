
# This module establishes several dev-op errors that are used in UserInput.py to handle user_inputted exceptions.
# These include such things as entering an odd number, entering a large number that may crash the system, etc.

class Error(Exception):
    pass


class NotGreaterThan2Error(Error):
    pass


class OddNumberError(Error):
    pass


class LargeNumberError(Error):
    pass


class NotYesOrNoError(Error):
    pass