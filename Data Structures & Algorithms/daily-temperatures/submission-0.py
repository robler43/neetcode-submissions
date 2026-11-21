"""
understand:

if no wormer day was recorded, return result[i] = 0

return result with (per day) the amount of days it took after that particular day for it to be warmer that day.

brute force:
loop for days,
    loop for each day compared to each day if value is greater or not
O n^2

improvvve:
have a stack
result array

loop through the array
    take ith element and move it onto the stack
    if the next element is greater:
        result ith postion is 1
    else:
        reuslt ith += 1
    


"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack  = [] #(temp, index)

        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res
