"""
Solve the tokens string in postfix notation
return the output

brute force:
would be to go through the array. 
add each string before an operator to a temporary string
once operator is reached
loop through each temporary stored number again and use the operator
O(n^2)


plan:
use stack []
res = 0
while not on end or array
    push element on stack
    if element == ("+", "-", "*", "/"):
        push operator on stack
        while !(stack.isEmpty()):
            res += operator(pop..)

return res



"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == ("+"):
                stack.append(stack.pop()+stack.pop())
            elif c == ("-"):
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == ("*"):
                stack.append(stack.pop()*stack.pop())
            elif c == ("/"):
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))

        return int(stack[0])
        