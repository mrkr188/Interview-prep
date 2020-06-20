
# ------------------------------ IMPORTANT ------------------------------
# follow binary_search_left and binary_search_right_ patterns for problems
# binary_search_left_ and binary_search_right are just for reference
# ------------------------------ IMPORTANT ------------------------------

# find index of leftmost occurance of target if there are duplicates
# or if element is not present return index of where to insert target
def binary_search_left(nums, target):
    n = len(nums)
    # for test case 3
    # this will return 1, to prevent this and get 2 use if target > nums[-1]: return len(n)
    if target > nums[-1]: 
        return n
    l, r = 0, n-1
    while l < r:
        m = l + (r-l)//2
        if nums[m] >= target: 
            r = m
        else: 
            l = m+1
    return l

print(binary_search_left([5,7,7,8,8,10], 8))
print(binary_search_left([5,7,7,8,8,10], 9))
print(binary_search_left([2,2], 3))  # this will return 1, to prevent this and get 2 use if target > nums[-1]: return len(n)
print(binary_search_left([3,4,7], 1))

# return index of leftmost occurance of target if there are duplicates
# or if element is not present return index of where to insert target
# when using l<=r use r=m. for l<r use r=m-1
def binary_search_left_(nums, target):
    n = len(nums)
    # if target > nums[-1]: 
    #     return n
    l, r = 0, n-1
    while l <= r:
        m = l + (r-l)//2
        if nums[m] >= target: 
            r = m-1
        else: 
            l = m+1
    return l

print(binary_search_left_([5,7,7,8,8,10], 8))
print(binary_search_left_([5,7,7,8,8,10], 9))
print(binary_search_left_([2,2], 3))
print(binary_search_left_([3,4,7], 1))


# find index of rightmost if there are duplicates
# or if element is not present return index of where to insert target
def binary_search_right(nums, target):
    n = len(nums)
    if target < nums[0]:
        return 0
    l, r = 0, n-1
    while l < r:
        # here we need to do additional +1 to m 
        # because sometimes when last occurance is found we wont get past it
        # in this example l=4 is last occurance, and r=5 while loop gets stuck at l=m part
        m = l + (r-l)//2 + 1
        if nums[m] <= target: 
            l = m
        else: 
            r = m-1
    return r if nums[r] == target else r+1

print(binary_search_right([5,7,7,8,8,10], 8))
print(binary_search_right([5,7,7,8,8,10], 9))
print(binary_search_right([2,2], 3))
print(binary_search_right([3,4,7], 1))



## for alternate solution - more easier to understand
## http://www.studyalgorithms.com/array/find-the-index-of-last-occurrence-of-an-element-in-a-sorted-array/



# alternate implementation to find index of rightmost occurance of target
def binary_search_right_(nums, target):

    # r becomes -1 when target < nums[0]
    if target < nums[0]:
        return 0

    l, r = 0, len(nums)-1
    while l <= r:
        # dont need +1 to m here
        m = l + (r-l)//2 
        if nums[m] <= target: 
            l = m+1
        else: 
            r = m-1
    # r=-1 when target < nums[0]
    # if r == -1: 
    #     return 0

    return r if nums[r] == target else r+1

print(binary_search_right_([5,7,7,8,8,10,11,12,15,20], 8))
print(binary_search_right_([5,7,7,8,8,10], 9))
print(binary_search_right_([2,2], 3))
print(binary_search_right_([3,4,7], 1))




# range of first and last occurance of target
def binary_search_range(nums, target):
    n = len(nums)
    if n<1:
        return -1,-1
    left, right = -1, -1
    l, r = 0, n-1
    while l <= r:
        m = l + (r-l)//2
        if nums[m] < target: 
            l = m+1
        else: 
            r = m-1
    if l>=n or nums[l] != target: return -1, -1
    left = l
    l, r = left, n-1
    while l <= r:
        m = l + (r-l)//2 
        if nums[m] == target: 
            l = m+1
        else: 
            r = m-1
    right = r
    return left, right


print(binary_search_range([5,7,7,8,8,8,10], 8))
print(binary_search_range([2,2], 3))
print(binary_search_range([3,4,7], 1))

# alternate implementation
def binary_search_range_(nums, target):
    n = len(nums)
    if n<1:
        return -1,-1
    left, right = -1, -1
    l, r = 0, n-1
    while l < r:
        m = l + (r-l)//2
        if nums[m] < target: 
            l = m+1
        else: 
            r = m
    if l>=n or nums[l] != target: return -1, -1
    left = l
    l, r = left, n-1
    while l < r:
        m = l + (r-l)//2 + 1
        if nums[m] == target: 
            l = m
        else: 
            r = m-1
    right = l
    return left, right


print(binary_search_range([5,7,7,8,8,8,10], 8))
print(binary_search_range([2,2], 3))
print(binary_search_range([3,4,7], 1))

