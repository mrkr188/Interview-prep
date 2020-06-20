# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

from collections import defaultdict

def lengthOfLongestSubstringTwoDistinct(s):
    
    n = len(s)
    
    left, right = 0, 0
    
    max_len = 0
    hashmap = defaultdict(int)
    
    while right < n:
        
        c = s[right]
        hashmap[c] = right
        right += 1
        
        if len(hashmap) == 3:
            ix = min(hashmap.values())
            del hashmap[s[ix]]
            left = ix+1
        
        # we dont do right-left+1 because we already did right += 1 above
        max_len = max(max_len, right-left)
    
    return max_len
            
print(lengthOfLongestSubstringTwoDistinct('eceba'))

print(lengthOfLongestSubstringTwoDistinct('ccaabbb'))
