
# a decorator to print function name and arguments
def print_func(func): 
    def inner_func(*args, **kwargs):
        
        print('{}{}'.format(func.__name__, args))
        
        return func(*args, **kwargs)

    return inner_func

# returns power set of numbers
def subsets(nums):
    if not nums: 
        return []
    @print_func
    def backtrack(index, path): 
        out.append(path[:])
        for i in range(index, len(nums)): 
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    out = []
    backtrack(0, [])
    return out
    
print(subsets([1,2,3]))
