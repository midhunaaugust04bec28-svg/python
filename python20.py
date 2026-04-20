The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of lowercase English letters. For a given integer , you can select any indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the indices selected will contain the letter: ''. 

code:



import itertools

# Read input
N = int(input())
letters = input().split()
K = int(input())

# 1. Generate all combinations of indices
all_combinations = list(itertools.combinations(range(N), K))

# 2. Identify indices where the letter 'a' is present (Fixed Syntax)
target_indices = {i for i, char in enumerate(letters) if char == 'a'}

# 3. Count combinations containing at least one target index
count = 0
for combo in all_combinations:
    # Check if any index in the combination is in our target set
    if any(index in target_indices for index in combo):
        count += 1

# 4. Print probability rounded to 4 decimal places
print(f"{count / len(all_combinations):.4f}")
