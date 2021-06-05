from http import HttpClient, Url
from utils import Utils
from enums import Type, Category, Difficulty


class Client:
    """"Represents a TrivIO client to connect to the opentdb.com Trivia API."""

    def __init__(self, use_token: bool = False):
        self.use_token = use_token

        self.utils = Utils()
        self.http = HttpClient(self.utils, use_token)

    async def request(self, _type: Type, amount: int = None, category: Category = None, difficulty: Difficulty = None):
        """"Returns the given amount of trivia questions."""

        url = Url(_type, amount, category, difficulty)

        return await self.http.request(url)

    async def close(self):
        """"Closes the Client and the connection to the api."""
        await self.http.close()

