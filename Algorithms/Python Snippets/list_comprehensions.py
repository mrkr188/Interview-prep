
# return a new string made of every other char starting with the first
# 'Heeololeo' → 'Hello'
# if condition
string = 'Heeololeo'
print(''.join((c for i,c in enumerate(string) if not i&1)))


# flatten list of list
# double loop
arr = [range(3), range(4), range(5)]
print([x for y in arr for x in y])







