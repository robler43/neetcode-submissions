"""
understand:
find the greatest solid area in given coordinates

brute force:
compare every height multiplied by each other
o(n^2)

plan:
data structure:
stacks [[ind, height] for heights] (to store width)
max var

if height i <= height i+1:
    stacks append i #because that means the 



"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []
        leftMost = [-1] *n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        stack = []
        rightMost = [n] *n

        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        maxArea= 0
        
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] +1))
        
        return maxArea