Your task is to sort the string in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234

Sample Output

ginortS1324
\






 code:

def sort_key(char):
    if char.islower():
        return (0, char)
    elif char.isupper():
        return (1, char)
    elif char.isdigit():
        if int(char) % 2 != 0:
            return (2, char)
        else:
            return (3, char)

s =input()
print("".join(sorted(s, key=sort_key)))


