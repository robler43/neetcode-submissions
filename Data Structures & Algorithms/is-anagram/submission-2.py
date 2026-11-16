class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        loop through s
        store if a new letter is in the dict, add a +1 to the count
        add a +1 count if the letter already exists

        same with t

        compare them (have to be same)
        """



        countS = {}
        countT = {}
        lengthS = len(s)
        lengthT = len(t)

        #base case
        if lengthS!=lengthT:
            return False


        for i in range(lengthS):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True


