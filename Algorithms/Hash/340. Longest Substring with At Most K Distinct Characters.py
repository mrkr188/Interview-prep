# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

from collections import OrderedDict

def lengthOfLongestSubstringKDistinct(s, k):
    n = len(s)
    if k == 0  or n == 0:
        return 0
    
    left, right = 0, 0
    
    hashmap = OrderedDict()
    max_len = 0
    
    while right < n:
        
        c = s[right]
        
        if c in hashmap:
            del hashmap[c]
        hashmap[c] = right
        right += 1
        
        if len(hashmap) == k+1:
            _, ix = hashmap.popitem(last=False)
            left = ix + 1
        
        max_len = max(max_len, right-left)
    
    return max_len

print(lengthOfLongestSubstringKDistinct("eceba", 2))

print(lengthOfLongestSubstringKDistinct("aa", 1))

