# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note:

# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Example 1:

# Input: 1
# Output: []
# Example 2:

# Input: 37
# Output:[]
# Example 3:

# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# Example 4:

# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]


def getFactors(n):
    
    if n<=3: 
        return []
    
    def backtrack(n, start, path):
        if n==1:
            if len(path)>1: 
                out.append(path[:])
            return 
        for i in range(start, n+1): 
            if n%i==0:
                path.append(i)
                backtrack(n//i, i, path)
                path.pop()
    out = []
    backtrack(n, 2, [])
    return out


print(getFactors(12))

print(getFactors(32))
