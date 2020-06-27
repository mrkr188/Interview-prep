
# Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example 1:

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:

# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]


def sortTransformedArray(nums, a, b, c):
    
    nums = [a*x*x+b*x+c for x in nums]
    
    left, right = 0, len(nums) - 1
    res = []
    
    while left <= right:
        
        if (a>0) ^ (nums[left]< nums[right]):
            res.append(nums[left])
            left += 1
            
        else:
            res.append(nums[right])
            right -= 1
            
    return res if a <= 0 else res[::-1]


print(sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5))

print(sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5))
