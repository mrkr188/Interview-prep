# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


def findMaxConsecutiveOnes(nums):
#         k = 1
#         left = 0
#         for right in range(len(nums)):
            
#             k -= 1-nums[right]
            
#             if k < 0:
#                 k += 1-nums[left]
#                 left += 1
                
#         return right - left + 1

    pre, curr, maxlen = -1, 0, 0
    for n in nums:
        if n == 0:
            pre, curr = curr, 0
        else:
            curr += 1
        maxlen = max(maxlen, pre + 1 + curr )
    
    return maxlen


print(findMaxConsecutiveOnes([1,0,1,1,0]))
