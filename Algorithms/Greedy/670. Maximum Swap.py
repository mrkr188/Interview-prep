
def maximum_swap(num):
    arr = list(map(int, str(num)))
    last = {x:i for i,x in enumerate(arr)}
    
    for i,x in enumerate(arr):
        for d in range(9, x, -1):
            if last.get(d, -1) > i:
                arr[i], arr[last[d]] = arr[last[d]], arr[i]
                return int(''.join(map(str,arr)))
    return num

print(maximum_swap(2736))
print(maximum_swap(9973))



# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.