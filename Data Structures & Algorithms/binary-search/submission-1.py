"""
find target within nums.
If it exists return its index from the array.
else return -1

O log n

brute force:
loop through array and compare to target
O n

Plan:
l and r pointer = 0 and len(nums)

while l<r:
    if nums[l] == target:
        return l
    elif nums[r] == target:
        return r
    l =/2
    r=/2

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l + r)//2
            
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
            
        return -1

                