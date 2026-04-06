from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows
        for i in range(9):
            if self.isArrayValid(self.getRow(board, i)) is False:
                return False
        
        # Check Cols
        for i in range(9):
            if self.isArrayValid(self.getCol(board, i)) is False:
                return False

        # Check Blocks
        for i in range(3):
            for j in range(3):
                if self.isArrayValid(self.getBlock(board, i, j)) is False:
                    return False

        return True

    def isArrayValid(self, arr: List[str]) -> bool:
        counter = Counter(arr)
        counter.pop(".", None)
        return all(val == 1 for val in counter.values())

    def getCol(self, board: List[List[str]], col_index) -> List[str]:
        col = []
        for i in range(9):
            col.append(board[i][col_index])
        return col

    def getRow(self, board: List[List[str]], row_index) -> List[str]:
        row = []
        for i in range(9):
            row.append(board[row_index][i])
        return row

    # Flattened, we don't care. Lol
    def getBlock(self, board: List[List[str]], block_row, block_col) -> List[str]:
        block = []
        for i in range(0 + 3 * block_row, 3 + 3 * block_row, 1):
            for j in range(0 + 3 * block_col, 3 + 3 * block_col, 1):
                block.append(board[i][j])
        return block
