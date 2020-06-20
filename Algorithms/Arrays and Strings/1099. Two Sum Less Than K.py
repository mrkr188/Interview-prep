# Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

# Example 1:

# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: 
# We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:

# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: 
# In this case it's not possible to get a pair sum less that 15.
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000

import math

def twoSumLessThanK(nums, k):
    nums.sort()
    
    l, r = 0, len(nums)-1
    res = -math.inf
    while l < r:
        s = nums[l] + nums[r]
        if s >= k:
            r -= 1
        elif s < k:
            res = max(res, s)
            l += 1
    return -1 if res == -math.inf else res

print(twoSumLessThanK([34,23,1,24,75,33,54,8], 60))

print(twoSumLessThanK([10,20,30], 15))
