from typing import Dict, Union, List, Optional

from .enums import Type, Difficulty


class Response:
    """
    This object represents a response from the api.

    Parameters
    -----------
    response_code: :class:`bool`
        The response code to indicate whether the results returned successfully.
    results: List[:class:`trivio.enums.Question`]
        The list of questions given by the result.
    token: :class:`str`
        The token returned by the request. This will mostly be None as this is only used for generating tokens.
        As the library handles the tokens this probably has no use case.

    """

    def __init__(self, data: Dict[str, Union[int, List[Dict[str, Union[str, List[str]]]]]]):
        self.response_code: int = data.get("response_code")
        self.token: Optional[str] = data.get("token")
        questions: List[Question] = []
        if data.get("results"):
            questions = [Question(question_data) for question_data in data.get("results")]
        self.results: List[Question] = questions


class Question:
    """
    This object represents a single question from an api call.

    Parameters
    -----------
    category: :class:`str`
        The category of the question.
    type: :class:`trivio.enums.Type`
        The type of the question
    difficulty: :class:`trivio.enums.Difficulty`
        The difficulty of this question.
    correct_answer: :class:`str`
        The correct answer of the question.
    wrong_answers: List[:class:`str`]
        The wrong answers to the question.

    """
    def __init__(self, data: Dict[str, Union[str, List[str]]]):
        self.category: str = data.get("category")
        self.type: Type = Type(data.get("type"))
        self.difficulty: Difficulty = Difficulty(data.get("difficulty"))
        self.question: str = data.get("question")
        self.correct_answer: str = data.get("correct_answer")
        self.wrong_answers: List[str] = data.get("incorrect_answers")

    @property
    def all_answers(self) -> List[str]:
        """
        Returns all answers for the question (correct and wrong).

        Returns
        --------
        List[:class:`str`]
            All the possible answers for the question.
        """
        return self.wrong_answers + [self.correct_answer]