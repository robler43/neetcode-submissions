'''
Understand:
find max volume of two upper boundaries

brute force;
compare every two values with another
return max output
o(n)

'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0

        while l<r:
            curr = min(heights[l],heights[r])*(r-l)
            maxArea = max(maxArea, curr)
            if heights[l]>heights[r]:
                r-=1
            elif heights[l]<=heights[r]:
                l+= 1
        return maxArea