class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in board:
            num_dict = {}
            for num in row:
                if num != ".":
                    num_dict[num] = num_dict.get(num, 0) + 1
                    if num_dict[num] > 1:
                        return False

        # Columns
        for c in range(9):
            col_dict = {}
            for r in range(9):
                num = board[r][c]
                if num != ".":
                    col_dict[num] = col_dict.get(num, 0) + 1
                    if col_dict[num] > 1:
                        return False

        # Boxes
        for box_r in range(3):
            for box_c in range(3):
                box_dict = {}
                for r in range(box_r * 3, box_r * 3 + 3):
                    for c in range(box_c * 3, box_c * 3 + 3):
                        num = board[r][c]
                        if num != ".":
                            box_dict[num] = box_dict.get(num, 0) + 1
                            if box_dict[num] > 1:
                                return False

        return True