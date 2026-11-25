"""
take input array with one to multiple row arrays in it

height = len(matrix)-1
width = len(matrix[0])-1
l,r = 0, height


while l<r:
    mid = (l + r) //2
    lVal = matrix[mid][0]
    rVal = matrix[mid][-1]
    while lVal <= target and rVal>=target:
        midVal = (lVal+rVal) // 2
        if midVal < target:
            lVal = midVal+1
        elif midVal > target:
            rVal = midVal-1
        else:
            return True
return False

while 

return if target exists

brute force:
o n^2 ----> m *n check every element with target


"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top,bot = 0, rows-1
        if matrix[0][0] == target:
            return True

        while top<=bot:
            row = (top + bot) //2 #row that were checking for target
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        
        if not (top<=bot):
            return False

        row = (top +bot)//2
        l, r= 0, cols-1
        while l<=r:
            m = (l+r) //2
            if target> matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True

        return False

