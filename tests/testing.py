import trivio
import asyncio


async def main():
    client = trivio.Client(True)
    questions = await client.request(trivio.Type.MULTIPLE_CHOICE, 1, trivio.Category.ALL, trivio.Difficulty.EASY)
    await client.close()
    print(questions)

asyncio.run(main())