import trivio
import asyncio


async def main():
    client: trivio.Client = trivio.Client(use_token=True)
    response: trivio.Response = await client.request(trivio.Type.MULTIPLE_CHOICE, 3, trivio.Category.ALL, trivio.Difficulty.EASY)
    await client.close()
    for index, question in enumerate(response.results, 1):
        print(f"Question {index}:")
        print(question.question)
        print("Answers:")
        print(" ".join(question.all_answers), "\n")


asyncio.run(main())