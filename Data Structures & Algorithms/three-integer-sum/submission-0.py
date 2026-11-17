"""
Take a nums array
find triplets that add up to 0
return a array with all the triplets inside
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #brute force
        #loop with 3 loops through each possible triplet
        #o n^3
        
        res = []
        nums.sort()

        for i,a  in enumerate(nums):
            #filter out duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            l, r= i+1, len(nums)-1
            
            while (l<r):
                threesum = a + nums[l]+ nums[r]
                if threesum< 0:
                    l+=1
                elif threesum> 0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+= 1
            
        return res