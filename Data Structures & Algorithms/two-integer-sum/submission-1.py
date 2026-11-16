"""
Understand:
- if there is two unique val that equal the target value
    -> output the index of these two ints of nums array
- i and j can not be the same index
- every input has exact one pair that satisfy the condition

Plan:
- brute force is o(n^2) - to compare every single nums value with every single value of nums

for i, j loop through nums where j is 1 ahead of i always
    if nums[i]+nums[j] == target:
        return [i,j]

hashmap = {} #val : index
for i,n in enumerate(nums):
    difference = target - nums[i]
    if diff in hashmap:
        return [hashmap[difference],i]
    else
        hashmap[n] = i
implement:


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #val : index
        for i,n in enumerate(nums):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference],i]
            else:
                hashmap[n] = i
