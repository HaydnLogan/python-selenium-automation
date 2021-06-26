"""

HW 5 Solution
4** Amazon interview question:
Create a function that will take a string as an input and retrun the 1st non-unique letter of a string.
"Google" => "l"
"Amazon" => "m"
If there are no unique letters, return an empty string: "xoxoxo" => "".
How would you test it>  How would you handle edge cases?

How to handle ""? => return Value Error
"""


def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    for l in string: # O(n)
        if string.count(l) == 1: # O(n)
            return l
    return ""
    # O(n) = O(n) = O(n^2)


print(unique_letter('google')) # llajhgjvv


def unique_letter_optimal(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    d = {}  # create dictionary
    # google
    for l in string: # O(n)
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for k, v in d.items():  # O(n)    Go through dictionary and find first value with value 1
        if v == 1:
            return k

    return ""


print(unique_letter_optimal('llajhgjvv'))