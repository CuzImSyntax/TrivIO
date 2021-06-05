import setuptools

setuptools.setup(
    name="TrivIO",
    version="0.1",
    license="MIT",
    author="CuzImSyntax",
    description="An async opentdb API wrapper written in python.",
    long_description="Coming Soon",
    long_description_content_type="text/markdown",
    url="https://github.com/CuzImSyntax",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.7.0',
    packages=setuptools.find_packages(where="trivio"),

)