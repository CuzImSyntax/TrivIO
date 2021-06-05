import aiohttp

from .enums import Type, Category, Difficulty


class Url:
    """"Represents a Url needed for making a request to the api"""

    Base_url = "https://opentdb.com/api.php?encode=base64"
    TOKEN_URL = "https://opentdb.com/api_token.php"

    def __init__(self,
                 is_command: bool,
                 _type: Type,
                 amount: int = None,
                 category: Category = None,
                 difficulty: Difficulty = None):

        self.is_command = is_command
        self._type = _type
        self.amount = amount
        self.category = category
        self.difficulty = difficulty

    @property
    def url(self):
        #Returns the url as a string
        if self.is_command:
            url = self.TOKEN_URL
            url += f"?command={self._type.value}"
            return url

        url = self.Base_url
        url += f"&type={self._type.value}"
        if self.amount:
            url += f"&amount={self.amount}"
        if self.category:
            url += f"&category={self.category.value}"
        if self.difficulty:
            url += f"&difficulty={self.difficulty.value}"
        return url


class HttpClient:
    """"Represents an HTTP client to send requests to the Open Trivia DB"""

    def __init__(self, utils, use_token: bool):
        self.utils = utils
        self.use_token = use_token
        self.token = None

        self._session = aiohttp.ClientSession()

    async def get_token(self):
        #Create a url object
        url = Url(True, Type.REQUEST)
        #get the token
        result = await self.request(url)
        return result["token"]

    async def request(self, url: Url):
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
        if data["response_code"] == 1:
            pass #ToDo raise No Results Could not return results. The API doesn't have enough questions for your query.
        elif data["response_code"] == 2:
            pass #ToDo raise  Invalid Parameter Contains an invalid parameter. Arguments passed in aren't valid.
        elif data["response_code"] in (3, 4):
            self.token = await self.get_token()
            return await self.request(_url)

        # Decode the data if necessary
        if "response_message" in data:
            return data

        return self.utils.build_dict(data)

    async def close(self):
        # Close the ClientSession if existing
        if self._session:
            await self._session.close()
