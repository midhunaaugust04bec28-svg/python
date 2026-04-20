You are given a function . You are also given lists. The list consists of elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

denotes the element picked from the list . Find the maximized value obtained.

denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem. 



code:

from itertools import product
K, M = map(int, input().split())
lists = []
for _ in range(K):
    row = list(map(int, input().split()))[1:]
    squared_row = [x**2 for x in row]
    lists.append(squared_row)
max_sum = 0
for combination in product(*lists):
    current_sum = sum(combination) % M
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

