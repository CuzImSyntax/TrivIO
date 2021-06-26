

class BaseError(Exception):
    """"The Base class for all Exceptions """

    pass


class NoResultFound(BaseError):
    """"Raised when the opentdb database hasn't enough questions for the given query."""

    def __init__(self):
        self.message = "There aren't enough questions in the database for your query"
        super.__init__(self.message)

    def __str__(self):
        return self.message


class InvalidParameter(BaseError):
    """"Raised when there is an invalid Parameter in the given query"""

    def __init__(self):
        self.message = "An invalid parameter was passed."
        super.__init__(self.message)

    def __str__(self):
        return self.message