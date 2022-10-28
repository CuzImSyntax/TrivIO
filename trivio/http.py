import aiohttp

from .enums import Type, Category, Difficulty
from .exceptions import NoResultFound, InvalidParameter, TokenEmpty
from .utils import Utils
from .models import Response


class Url:
    """Represents an Url needed for making a request to the api

    Parameters:
    -----------
    is_command: :class:`bool`
        Whether the Url should be for a command call.
    _type: :class:`trivio.Type`
        Determines whether returned questions should be multiple choice or yes/no questions.
    amount: :class:`int`
        The number of questions that should be returned the number of returned questions must be between 1 and 50.
    category: Optional[:class:`trivio.Category`]
        The category of the returned questions. When leaving empty there will be questions from a random category.
    difficulty: Optional[:class:`trivio.Difficulty`]
        The difficulty of the returned questions. When leaving empty there will be questions from all difficulties.
    """

    BASE_URL = "https://opentdb.com/api.php?encode=base64"
    TOKEN_URL = "https://opentdb.com/api_token.php"

    def __init__(self,
                 is_command: bool,
                 _type: Type,
                 amount: int = None,
                 category: Category = None,
                 difficulty: Difficulty = None):

        self.is_command: bool = is_command
        self._type: Type = _type
        self.amount: int = amount
        self.category: Category = category
        self.difficulty: Difficulty = difficulty

    @property
    def url(self):
        """:class:`str`: Returns the url as a string."""
        if self.is_command:
            url = self.TOKEN_URL
            url += f"?command={self._type.value}"
            return url

        url = self.BASE_URL
        url += f"&type={self._type.value}&amount={self.amount}"
        if self.category:
            url += f"&category={self.category.value}"
        if self.difficulty:
            url += f"&difficulty={self.difficulty.value}"
        return url


class HttpClient:
    """Represents an HTTP client to send requests to the Open Trivia DB

    Parameters:
    -----------
    utils: :class:`trivio.Utils`
        A instance of the Utils class
    use_token: Optional[:class:`bool`]
        Determines whether the client should use a session token or not.
        When this is enabled, the http Client will automatically regenerate the token when the token is invalid
        or all questions were returned.
    """
    def __init__(self, use_token: bool):
        self.utils: Utils = Utils()
        self.use_token: bool = use_token
        self.token = None

        self._session = aiohttp.ClientSession()

    async def get_token(self):
        """Gets a token from the opentdb api."""

        #Create a url object
        url = Url(True, Type.REQUEST)
        #get the token
        result: Response = await self.request(url)
        return result.token

    async def request(self, url: Url) -> Response:
        """|coro|

        Makes a http request to the opentdb api.

        Parameters:
        -----------
        url: :class:`Url`
            The url object to make the request with.

        Returns:
        -----------
        :class:`list`
            The requested questions in a list.
        """
        _url = url.url

       #Check if we should use a token
        if not url.is_command:
            if self.use_token:
                self.token = await self.get_token()
                if self.token:
                    _url += f"&token={self.token}"

        #make the request
        async with self._session.request("get", _url) as r:
            data = await r.json()

        #Cheking the response codes from the api
        if data["response_code"] == 0:
            # Decode the data if necessary
            if "response_message" in data:
                return Response(data)

            return Response(self.utils.build_list(data))

        await self.close()
        if data["response_code"] == 1:
            raise NoResultFound()
        elif data["response_code"] == 2:
            raise InvalidParameter()
        elif data["response_code"] == 3:
            self.token = await self.get_token()
            return await self.request(url)
        elif data["response_code"] == 4:
            raise TokenEmpty()

    async def close(self):
        """|coro|

        Close the ClientSession if existing"""
        if self._session:
            await self._session.close()
