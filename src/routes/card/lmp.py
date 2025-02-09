from pydantic import BaseModel
from johnllm import LMP

from src.question import QuestionsList

# TODO: should probably split up verification generation to another separate step
# since we need to account for different types of verifiers
class CreateQuestions(LMP):
    prompt = """
You are tasked to take the following conversation and generate a list of questions:
{{conversation}}

Your response should be a list of questions in the form: 
class Question(BaseModel):
    is_concept: bool
    question: str
    answer_type: AnswerType
    tags: list[str] | None = None

Arguments:
** is_concept: Can the question be parameterized with different values to formulate 
a similar question that tests the same concept?
Examples: 
    Math problems -> is_concept=True, because variables can be changed
    Recall Q/A problems -> is_concept=False, because the answer is fixed
** question: The actual question string. If is_concept == True, the question should be a conceptual question
that avoids specific values. Also, be as specific as possible to the possible forms that these values can take
Examples:
    Instead of "What is 2 + 2?", use "What is x + y where x and y are integers?"
    Instead of "Write a function to find the sum of the numbers in the list [1, 2, 3, 4, 5]" use "Write a function to find the sum of the numbers in a given list of integers"
BUT REMEMBER. Only do this is is_concept == True
** answer_type: The of answer expected. This can be:
class AnswerType(Enum):
    SA_DETERM = "sa_determ"
    SA_PROB = "sa_prob"
SA_DETERM: Short answer, deterministic. Math and coding problems
SA_PROB: Short answer, probabilistic. Requires semantic matching ie.
"Who as the main instigator of the Napoelonic Wars?" -> "Napoleon" and "Bonaparte" are both correct answers
and requires a semantic verifier to check
** answer_kind: The Type of the answer expected. Use Python type annotation syntax to denote this
Examples:
    int, str, List[int], List[str], Dict[str, int]
""" 
    response_format = QuestionsList


class VerifierFunction(BaseModel):
    func: str

class CreateVerifier(LMP):
    prompt = """
{{question}}

Given the question above, generate a Python function that can be used to verify the answer
This function should be able to verify the correctness for all cases where create a specific instance of the question
is created using create_card_prompt 
"""
    response_format = VerifierFunction

class ReviewCard(BaseModel):
    front: str
    back: str

class GenerateCard(LMP):
    prompt = """
{{question}}

Given the question above, generate an spaced repetition card that can be used to study this question
If the question given is a conceptual problem, remember to create a specific instantiation of the concept in your review card
"""
    response_format = ReviewCard