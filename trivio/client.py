from .http import HttpClient, Url
from .utils import Utils
from .enums import Type, Category, Difficulty


class Client:
    """Represents a TrivIO client to connect to the opentdb.com Trivia API.

    There's one option that can be passed to the :class:`Client`.
    Parameters
    -----------
    use_token: Optional[:class:`bool`]
        Determines whether the client should use a session token or not.
        Session Tokens are unique keys that will help keep track of the questions the API has already retrieved.
        By appending a Session Token to a API Call, the API will never give you the same question twice.
        Over the lifespan of a Session Token, there will eventually reach a point where you have exhausted
        all the possible questions in the database. At this point the api will automatically create a new token for you.
        """

    def __init__(self,
                 use_token: bool = False):

        self.use_token = use_token

        self.utils = Utils()
        self.http = HttpClient(self.utils, self.use_token)

    async def request(self,
                      _type: Type,
                      amount: int,
                      category: Category = None,
                      difficulty: Difficulty = None):
        """|coro|

        Makes a request to the trivia api and returns questions according to the given query
        Parameters
        -----------
        _type: :class:`Type`
            Determines whether returned questions should be multiple choice or yes/no questions.
        amount: :class:`int`
            The number of questions that should be returned the number of returned questions must be between 1 and 50.
        category: Optional[:class:`Category`]
            The category of the returned questions. When leaving empty there will be questions from a random category.
        difficulty: Optional[:class:`Difficulty`]
            The difficulty of the returned questions. When leaving empty there will be questions from all difficulties.

        Returns
        --------
        :class:`list`
            The requested questions in a list.
        """

        url = Url(False, _type, amount, category, difficulty)

        return await self.http.request(url)

    async def close(self):
        """|coro|

        Closes the Client and the connection to the api."""
        await self.http.close()

