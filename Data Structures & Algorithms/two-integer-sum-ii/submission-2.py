class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force is to check every set of numbers with each other if they equal the target (o n^2)

        l, r = 0, len(numbers) -1

        while l<r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -=1
            elif currSum< target:
                l += 1
            
            if currSum == target:
                return [l +1, r+1]
