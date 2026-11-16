class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        for f in nums:
            '''
            understand:
            brute force: o(n log n):
            go through the array, store the count of each number
            then call the k'th most frequent value

            use hashset to store each number and their count

            loop through the array given
                if value not in hashset:
                    add num as key in hashset and 
                else:
                    store key i in hashset with value = 1
            
            add the keys to a max heap until kth largest

            return heap(k)
            '''

            count = {}
            freq = [[] for i in range(len(nums) +1)]

            for n in nums:
                count[n] = 1 + count.get(n,0)
            for n, c in count.items():
                freq[c].append(n)

            res = []
            for i in range(len(freq) - 1, 0, -1):
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
