from pydantic import BaseModel
from typing import List, Any
from abc import ABC, abstractmethod
from enum import Enum

# TODO: for code verifiers, tricky because:
# 1. Executing potentially unsafe code
# 2. Need an environment with pre-installed packages
# -> actually this might be good monetization advantage
#
# Check out judge0: https://github.com/judge0
# In actual deployment the verifier would live on a separate server
class Verifier(BaseModel, ABC):
    """Initialize state, such as grabbing an interpreter to run code"""
    @abstractmethod
    def verify(self, response: str) -> bool:
        pass

class Card:
    pass

class AnswerType(Enum):
    SA_DETERM = "sa_determ"
    SA_PROB = "sa_prob"

# TODO: figure out if instructor takes into account docstrings in model
# definition prompt
class Question(BaseModel):
    is_concept: bool
    question: str
    answer_type: AnswerType
    answer_kind: Any
    verifier: str | None = None
    tags: list[str] | None = None
        
class QuestionsList(BaseModel):
    questions: List[Question]