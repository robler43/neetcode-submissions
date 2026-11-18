"""
Every open bracket in input string has to ave a closing one
They are in order

brute force:
compare element 1 with last one
    if they equal move on


plan:
base case:
if len(string) % 2 != 0
    return False

create a stack
loop i through len string add element i on stack
    while i < len string/2:
        if  and i == ( "{" or "[" or "(":
            .push
    if i == ( "}" or "]" or ")":
        if stack.pop == stack[i-1]:
            continue
        else:
            return False
return True


"""

class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = { ")":"(" , "}":"{" , "]":"["}
        stack = []

        for i in s:
            if i in closedToOpen:
                if stack and (stack[-1] == closedToOpen[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return True if not stack else False

