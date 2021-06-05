import aiohttp

from enums import Type, Category, Difficulty


class Url:
    """"Represents a Url needed for making a request to the api"""

    Base_url = "https://opentdb.com/api.php&encode=base64"

    def __init__(self, is_command: bool, _type: Type, amount: int = None, category: Category = None, difficulty: Difficulty = None):
        self.is_command = is_command
        self._type = _type
        self.amount = amount
        self.category = category
        self.difficulty = difficulty

    @property
    def url(self):
        #Returns the url as a string

        url = self.Base_url

        if self.is_command:
            url += f"?command={self._type}"
            return url

        url += f"?type={self._type}"
        if self.amount:
            url += f"?amount = {self.amount}"
        if self.category:
            url += f"?category={self.category}"
        if self.difficulty:
            url += f"?difficulty={self.difficulty}"
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
        return self.request(url)

    async def request(self, url: Url):
        url = url.url

       #Check if we should use a token
        if self.use_token:
            self.token = await self.get_token()
            if self.token:
                url += f"?token={self.token}"

        #make the request
        async with self._session.request("get", url) as r:
            data = await r.json()
            if 3 <= data["response_code"] <= 4:
                self.token = await self.get_token()
                return await self.request(url)

            #Decode the data if necessary
            if "response_message" in data:
                return data
            return self.utils.decode(data)

    async def close(self):
        # Close the ClientSession if existing
        if self._session:
            await self._session.close()
