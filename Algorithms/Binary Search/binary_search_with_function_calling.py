# this pattern of binary search is used when we use return value from function at mid point to make decisions
# like, if fun(mid) == True


# lets assume we have return values from function in this array
a = [True, True, True, True, False, False, False, False, False]

# pattern 1
# find the first False value - ans = 4
# this is like finding the left most point where return value from function is true
# used in 278. First Bad Version - https://leetcode.com/problems/first-bad-version/
l,r = 1,n
while l <= r:
    m = l + (r-l)//2
    if isBadVersion(m):
        r = m-1
    else:
        l = m+1
return l
# return value
print(l)



# pattern 2
# find last True value - ans = 3
# this is like finding the right most point where return value from function is true
# used in 1062. Longest Repeating Substring - https://leetcode.com/problems/longest-repeating-substring/
l, r = 0, len(a)-1
while l <= r:
    m = l + (r-l)//2
    if a[m] == True:
        l = m+1
    else:
        r = m-1
# return value
print(l-1)





