"""
understand:
given an array
find all groups of words that contain the same letters. order doesnt matter


return the output array

brute force (worst case):
- compare every one string and its contents letters to every string in the array
O(n^2 * k) (k average elements per string, n strings)

use hashmap
add 

if len(s) == len(t):

loop through array i
    add letters to hashmap_1
    add letters of string 2 to hashmap_2
    if hashmap1 == hashmap2
        store anogram in []
        store anogram in all_anagram []
    

"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] *26

            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        
        return list(res.values())
