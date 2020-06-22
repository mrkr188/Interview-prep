# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

# Some examples:

# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

# Note: Do not use the eval built-in library function.

def calculate(s):
    
    s = s + '!'
    def helper(stack, i):
        num = 0
        sign = '+'
        while i < len(s):
            
            c = s[i]
            
            if c == " ":
                i += 1
                continue
                
            if c.isdigit():
                num = 10 * num + int(c)
                i += 1
                
            elif c == '(':
                num, i = helper([], i+1)
                
            else:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                i += 1
                if c == ')':
                    return sum(stack), i
                sign = c 
                
        return sum(stack), i
    
    res, _ = helper([], 0)
    
    return res


print(calculate("1 + 1"))

print(calculate(" 6-4 / 2 "))

print(calculate("2*(5+5*2)/3+(6/2+8)"))

print(calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))

