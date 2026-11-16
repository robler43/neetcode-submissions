class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        understand:
        return the two positions that add up to the target variable

        plan:
        create hashmap , store each nums in there


        loop i through nums
        hashset += i

        return in hashset:
                return [i, (target-i)]

            implement:

        """


        hashmap = {}

        for i, n in enumerate(nums):
            subtraction = target - n
            if subtraction in hashmap:
                return [hashmap[subtraction], i]
            hashmap[n] = i
        return