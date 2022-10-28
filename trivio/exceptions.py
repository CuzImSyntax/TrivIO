class BaseError(Exception):
    """"The Base class for all Exceptions """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class NoResultFound(BaseError):
    """Raised when the opentdb database hasn't enough questions for the given query."""

    def __init__(self):
        message = "There aren't enough questions in the database for your query"
        super().__init__(message)


class TokenEmpty(BaseError):
    """
    Raised when the token has returned all possible questions for the specified query. Resetting the token is necessary.

    .. note::
        This can also mean that there aren't enough results in the opentdb database. For some reason the API also raises
        does not raise :class:`NoResultFound` in this case.
    """
    def __init__(self):
        message = "The token has returned all possible questions for the specified query. " \
                       "This can also mean there aren't enough questions in the database for your query."
        super().__init__(message)


class InvalidParameter(BaseError):
    """"Raised when there is an invalid Parameter in the given query"""

    def __init__(self):
        message = "An invalid parameter was passed."
        super().__init__(message)