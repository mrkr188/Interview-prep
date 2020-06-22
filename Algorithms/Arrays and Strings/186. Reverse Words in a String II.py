# Given an input string , reverse the string word by word. 

# Example:

# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note: 

# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?


def reverseWords(s):
    """
    Do not return anything, modify s in-place instead.
    """
    
    def reverse(l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
            
    n = len(s)
    left = right = 0
    
    reverse(s, 0, n-1)
    
    while right < n:
        
        while right < n and s[right] != ' ':
            right += 1
        
        reverse(s, left, right-1)
        
        left = right + 1
        right = right + 1

    return s

print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))

   