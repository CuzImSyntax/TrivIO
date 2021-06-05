import trivio
import asyncio


async def main():
    client = trivio.Client(True)
    result = await client.request(trivio.Type.TRUE_FALSE, 1, trivio.Category.ART, trivio.Difficulty.EASY)
    await client.close()
    print(result)


asyncio.run(main())