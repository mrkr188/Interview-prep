
# when you want to go back 
# useful in - 139. Word Break https://leetcode.com/problems/word-break/
current_pointer = 10
shift_backwords = 4
print('starting pointer would be', current_pointer-shift_backwords+1) 


# loop for merging all elements in list of lists
# used in merge k sorted lists case
length = 9
interval = 1
while interval < length:
    for i in range(0, length-interval, interval*2):
        print(i, i+interval)
    interval *= 2


