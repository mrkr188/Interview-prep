# Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

# Example 1
# Input:

# 48 
# Output:
# 68
# Example 2
# Input:

# 15
# Output:
# 35


def smallestFactorization(a):
    if a < 2:
        return a

    res = 0
    multiplier = 1
    
    for i in range(9, 1, -1):
        while a%i == 0:
            a //= i
            res = multiplier*i + res
            multiplier *= 10
    
    return res if a == 1 and res < 2**31-1 else 0


print(smallestFactorization(48))

print(smallestFactorization(15))
