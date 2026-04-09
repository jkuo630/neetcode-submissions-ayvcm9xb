class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def containsDuplicate(nums: list[str]) -> bool:
            seen = set()
            for num in nums:
                if num == ".":
                    continue
                if num in seen:
                    return True 
                seen.add(num)
            return False 
        
        # check one 
        for row in board:
            if containsDuplicate(row):
                return False

        # check two
        cols = {}        
        for r in range(9):
            for c in range(9):
                if c not in cols:
                    cols[c] = []
                cols[c].append(board[r][c])

        for lst in cols.values():
            if containsDuplicate(lst):
                return False

        # check three
        squares = {}     
        for r in range(9):
            for c in range(9):
                square_key = (r // 3, c // 3)
                if square_key not in squares:
                    squares[square_key] = []
                squares[square_key].append(board[r][c])
        
        for lst in squares.values():
            if containsDuplicate(lst):
                return False

        return True 
        