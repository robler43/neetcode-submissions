class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #board is a list argument

        #check if each 3x3 has duplicates


        #if not: check if any column 9x9 has duplicates (1-9)
        # if not: check if any row 9x9 has duplicates (1-9)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # (r // 3 , c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True