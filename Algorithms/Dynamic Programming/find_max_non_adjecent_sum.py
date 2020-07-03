
import math

def find_max_non_adjecent_sum(nums):

    incl, excl = nums[0], 0
    for num in nums[1:]:
        new_excl = max(excl, incl)
        incl = excl + num
        excl = new_excl 
    
    return max(incl, excl)

print(find_max_non_adjecent_sum([2, 4, 6, 2, 5]))

print(find_max_non_adjecent_sum([5, 1, 1, 5]))

print(find_max_non_adjecent_sum([-5, -1, -1, -5, 0]))

