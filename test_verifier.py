from src.routes.card.lmp import CreateVerifier

from johnllm import LLMModel

QUESTION = """
is_concept=True 
question='What is the dot product of two vectors x and y?' 
answer_type=<AnswerType.SA_DETERM: 'sa_determ'> 
verifier=None 
create_card_prompt='Generate a dot product problem using two 2-element integer vectors.' 
tags=['vector mathematics', 'dot product', 'linear algebra', 'basic operations']
"""

lm = LLMModel()
res = CreateVerifier().invoke(lm, model_name="gpt-4o", question=QUESTION)
print(res.func)