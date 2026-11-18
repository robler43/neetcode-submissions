'''
understand:
map array given. (height and position)
calculate trapped areas
return total of trapped area

brute force:
o(n^2) calculate the area between every height value with each value

plan:
slow, fast pointer = 0,2
sumArea = 0

while fast<len(height)-1
    base cases
    if fast is == slow.next() or fast == slow:
        fast increment
    
    check if slow,fast is 0
        increment that pointer

    if height[fast+1]>height[fast]:
        fast+=1
    else:
        sumArea = min(height[l], height[r])*(r-l)
        slow = fast
        fast += 2

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0 , len(height)-1
        leftMax, rightMax = height[l], height[r]
        res= 0

        while l<r:
            if leftMax<rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res

            