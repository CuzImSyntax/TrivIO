import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

packages = ["trivio"]

setuptools.setup(
    name="trivio",
    version="0.1",
    license="MIT",
    author="CuzImSyntax",
    description="An async opentdb API wrapper written in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CuzImSyntax/TrivIO",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.7.0',
    install_requires=requirements,
    packages=packages

)