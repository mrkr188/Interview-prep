# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# Example:

# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]


def findMissingRanges(nums, lower, upper):
        
#         def add_range(x,y, res=[]):
#             diff = y-x
#             if diff == 2:
#                 return res.append(str(x+1))
#             elif diff > 2  :
#                 return res.append(str(x+1) + '->' + str(y-1))
    
#         res = []
#         if not nums:
#             add_range(lower-1, upper+1, res)
#             return res
    
#         add_range(lower-1, nums[0], res)
#         for i in range(len(nums)-1):
#             add_range(nums[i], nums[i+1], res)
#         add_range(nums[-1], upper+1, res)
        
#         return res

    result = []
    nums.append(upper+1)
    pre = lower - 1
    for i in nums:
        if (i == pre + 2):
            result.append(str(i-1))
        elif (i > pre + 2):
            result.append(str(pre + 1) + "->" + str(i -1))
        pre = i
    return result


print(findMissingRanges(nums = [0, 1, 3, 50, 75], lower = 0, upper = 99))
