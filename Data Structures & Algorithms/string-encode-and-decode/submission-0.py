class Solution:

    def encode(self, strs: List[str]) -> str:
        #store the strings in one string
        res = ""
        #loop through the strs to add each string to the same string and add the len of each string as a string before the string gets added to the result. add a # symbol to separate strings to keep track of count
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #read the result string
        #check the first number in the string to get the length
        #loop through that string, after # symbol, for the according length
            #store that string as a string in str List
        #do it all over again with the next 
        res, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            lengthWord = int(s[i:j])

            res.append(s[j+1 : j+1+lengthWord])
            i=j+1 +lengthWord
        return res
