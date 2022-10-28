Example
============

The following is just a very simple example.
We setup a Client which is used to talk to the API.
then we get 10 easy multiple choice questions from all available categories.
We then just print the questions and all possible answers to the terminal.

.. code:: python3

    import trivio
    import asyncio

    async def main():

        client: trivio.Client = trivio.Client(use_token=True)
        questions: trivio.Response = await client.request(trivio.Type.MULTIPLE_CHOICE, 10, trivio.Category.ALL, trivio.Difficulty.EASY)
        await client.close()
        if questions.results:
            print(questions.results[0].question)
            print(questions.results[0].all_answers)

    asyncio.run(main())
