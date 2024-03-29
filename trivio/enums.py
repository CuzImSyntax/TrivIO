from enum import Enum

__all__ = ["Type", "Category", "Difficulty"]


class Type(Enum):
    """The Different Types of questions, to get questions from."""

    MULTIPLE_CHOICE = "multiple"
    TRUE_FALSE = "boolean"
    REQUEST = "request"

    def __str__(self):
        return self.value


class Category(Enum):
    """The Different Categories, to get questions from."""

    ALL = 0
    GENERAL_KNOWLEDGE = 9
    BOOKS = 10
    FILM = 11
    MUSIC = 12
    MUSICALS_THEATRES = 13
    TELEVISION = 14
    VIDEO_GAMES = 15
    BOARD_GAMES = 16
    SCIENCE_NATURE = 17
    COMPUTERS = 18
    MATHEMATICS = 19
    MYTHOLOGY = 20
    SPORTS = 21
    GEOGRAPHY = 22
    HISTORY = 23
    POLITICS = 24
    ART = 25
    CELEBRITIES = 26
    ANIMALS = 27
    VEHICLES = 28
    COMICS = 29
    GADGETS = 30
    ANIME_MANGA = 31
    CARTOON_ANIMATIONS = 32


class Difficulty(Enum):
    """The Different Difficulties, to get questions from."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __str__(self):
        return self.value