# TrivIO

An async opentdb API wrapper written in python.

## Installation
The repo isn't on pypi yet as it's still in an early dev stage.

if you want to use the current version you can install it manually

```bash
git clone https://github.com/CuzImSyntax/TrivIO
cd TrivIO
python setup.py install
```

##Docs
Im currently working on the documentation.

It will probably be available in a few weeks.

##Simple Example

```python
import trivio
import asyncio

async def main():
    #
    client = trivio.Client(True)
    questions = await client.request(trivio.Type.MULTIPLE_CHOICE, 1, trivio.Category.ALL, trivio.Difficulty.EASY)
    await client.close()
    print(questions)

asyncio.run(main())
```

## Contributing
Contributions are welcome, when you want to make major changes, feel free to open an issue first to discuss the changes


