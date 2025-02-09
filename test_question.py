from src.routes.card.lmp import (
    CreateQuestions, 
    CreateVerifier,
    GenerateCard
)

from johnllm import LLMModel

CONVO = """
Level 1: Basic Vector Dot Product

Problem: What is the dot product of two vectors [1, 2] and [3, 4]?
Skills: Understanding element-wise multiplication and summation
Resolution: Very fuzzy (introduces only the most basic operation needed)

Level 2: 2D Row-Column Multiplication

Problem: Given matrix A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], calculate the element at position (0,0) of the resulting matrix
Skills: Applying dot product to matrix rows and columns
Resolution: Clearer but still simplified (introduces matrix position concept)

Level 3: Complete 2D Matrix Multiplication

Problem: Multiply two 2×2 matrices A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]]
Skills: Systematically applying row-column multiplication across all positions
Resolution: Medium (complete 2D operation)

Level 4: Single Layer of 3D Multiplication

Problem: Given the first layer of A (2×3×2) and first layer of B (2×2×3), calculate one element of the result
Skills: Understanding how 2D operations extend to one layer of 3D
Resolution: Higher (introduces 3D concept but limited scope)

Level 5: Cross-Layer Element Calculation

Problem: Calculate C[0,0,0] using both layers of A and B, where A is (2×3×2) and B is (2×2×3)
Skills: Understanding how elements from different layers interact
Resolution: Very high (full depth operation but single element)

Level 6: Complete Single Position

Problem: Calculate all elements C[i,j,k] where i=0, j=0 for all k, using complete matrices A (2×3×2) and B (2×2×3)
Skills: Systematically applying cross-layer calculations for a fixed position
Resolution: Nearly complete (multiple elements but fixed position)

Level 7: Full 3D Matrix Multiplication

Problem: Complete multiplication of A (2×3×2) and B (2×2×3) to get C (2×3×3)
Skills: Integrating all previous concepts for full operation
Resolution: Complete (full problem)

For each level, here are example practice questions:
Level 1:

What's [1, 2] · [3, 4]?
What's [2, 3] · [1, 2]?

Level 2:

Calculate result[0,0] for [[1, 2], [3, 4]] × [[5, 6], [7, 8]]
Calculate result[1,0] for the same matrices

Level 3:

Multiply [[1, 2], [3, 4]] × [[5, 6], [7, 8]]
Multiply [[2, 0], [1, 3]] × [[1, 4], [2, 5]]

Level 4:

Calculate C[0,0,0] using only first layers of A and B
Calculate C[0,1,0] using only first layers

Level 5:

Calculate C[0,0,0] using both layers of A and B
Calculate C[0,0,1] using both layers

Level 6:

Calculate C[0,0,:] (all k values for i=0, j=0)
Calculate C[1,0,:] (all k values for i=1, j=0)

Level 7:

Complete full multiplication of given matrices
Verify result matches using numpy's implementation
"""

CONVO_SHORT = """
Level 1: Basic Vector Dot Product

Problem: What is the dot product of two vectors [1, 2] and [3, 4]?
Skills: Understanding element-wise multiplication and summation
Resolution: Very fuzzy (introduces only the most basic operation needed)

Level 2: 2D Row-Column Multiplication

Problem: Given matrix A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], calculate the element at position (0,0) of the resulting matrix
Skills: Applying dot product to matrix rows and columns
Resolution: Clearer but still simplified (introduces matrix position concept)

For each level, here are example practice questions:
Level 1:

What's [1, 2] · [3, 4]?
What's [2, 3] · [1, 2]?

Level 2:

Calculate result[0,0] for [[1, 2], [3, 4]] × [[5, 6], [7, 8]]
Calculate result[1,0] for the same matrices
"""


lm = LLMModel()
res = CreateQuestions().invoke(lm, model_name="gpt-4o", conversation=CONVO_SHORT)

for q in res.questions:
    print(q)
    res = CreateVerifier().invoke(lm, model_name="gpt-4o", question=(str(q)))
    print(res.func)
    card_res = GenerateCard().invoke(lm, model_name="gpt-4o", question=(str(q)))
    
    print(card_res.front)
    print(card_res.back)


    break