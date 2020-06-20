# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:

# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?

from collections import defaultdict

def maxSubArrayLen(nums, k):
    res = 0
    acc = 0              

    h = defaultdict(int)

    for i in range(len(nums)):
        acc += nums[i]
        if acc not in h:
            h[acc] = i 
            
        if acc == k:    #everything from 0, to i has been aggregated to add up to k. Length = i-0+1
            res = max(res, i-0+1)
        elif acc-k in h:    # everything from i-h[acc-k] to i add up to k
            res = max(res, i-h[acc-k])                

    return res


print(maxSubArrayLen(nums = [1, -1, 5, -2, 3], k = 3))

print(maxSubArrayLen(nums = [-2, -1, 2, 1], k = 1))
