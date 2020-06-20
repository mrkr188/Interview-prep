# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example:

# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1]
#              [-2,0,3]
# Follow up: Could you solve it in O(n2) runtime?

def threeSumSmaller(nums, target):
    
    nums.sort()
    n = len(nums)
    res = 0
    
    for i in range(n):
        l, r = i+1, n-1
        # to exclude repeted triplet
        # if i > 0 and nums[i-1] == nums[i]:
        #     continue
        while l < r:
            s = nums[l] + nums[r] + nums[i]
            if s < target:
                res += r-l
                l += 1
            else:
                r -= 1
    return res


print(threeSumSmaller(nums = [-2,0,1,3], target = 2))
