import trivio
import asyncio


async def main():
    client = trivio.Client(use_token=True)
    questions = await client.request(trivio.Type.TRUE_FALSE, 10, trivio.Category.ART, trivio.Difficulty.HARD)
    await client.close()
    print(questions)

asyncio.run(main())