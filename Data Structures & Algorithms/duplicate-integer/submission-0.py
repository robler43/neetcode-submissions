class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        
        for var in nums:
            if var in visited:
                return True

            visited.append(var)

        return False