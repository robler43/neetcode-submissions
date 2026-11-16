#take array nums
#return length of longest consecutive sequence of elements that can be formed. 

"""
brute force:
take each element in the array.
check with each element if there is one element in the array that is 1 greater
store the length as +1 of that consecutive sequence
return the length of the longest sequence
o(n^2)

"""



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
    
        for number in nums:
            #checkl if number is start of a sequence
            if (number-1) not in hashset:
                length = 0
                while (number+length in hashset):
                    length+= 1

                longest = max(length, longest)
            
        
        return longest