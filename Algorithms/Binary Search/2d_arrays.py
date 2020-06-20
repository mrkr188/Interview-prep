x = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# rows and cols
print(len(x), 'rows, ', len(x[0]), 'cols')

# print rows
for i in x:
    print(i)

# print cols
for i in zip(*x):
    print(i)

