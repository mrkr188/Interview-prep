# Given a non-negative integer num, Return its encoding string.

# The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:

# g(0) = "" 
# g(1) = "0" 
# g(2) = "1" 
# g(3) = "00" 
# g(4) = "01" 
# g(5) = "10" 
# g(6) = "11"
# g(7) = "000"

# Example 1:

# Input: num = 23
# Output: "1000"
# Example 2:

# Input: num = 107
# Output: "101100"



def encode(num):
    # "1" + f(num) = binary(num + 1)
    return bin(num+1)[3:]


print(encode(23))

print(encode(107))

