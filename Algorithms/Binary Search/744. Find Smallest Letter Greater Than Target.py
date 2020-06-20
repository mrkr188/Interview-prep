
def next_greatest_letter(letters, target):
    if target < letters[0]:
        return letters[0]
    n = len(letters)
    l, r = 0, n-1
    while l < r:
        m = l + (r-l)//2 + 1
        if letters[m] <= target: 
            l = m
        else: 
            r = m-1
    return letters[(r+1) % n]

print(next_greatest_letter(['c', 'f', 'j'], 'a'))
print(next_greatest_letter(['c', 'f', 'j'], 'd'))
print(next_greatest_letter(['c', 'f', 'j'], 'k'))

# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.