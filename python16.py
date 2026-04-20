In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively times in the string. Replace these consecutive occurrences of the character '' with in the string.

For a better understanding of the problem, check the explanation. 




code:

from itertools import groupby
s =input()
for k, g in groupby(s):
    print(f"({len(list(g))}, {k})", end=" ")
