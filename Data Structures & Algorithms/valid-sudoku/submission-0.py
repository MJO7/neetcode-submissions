class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(array_for_checking):
            for i in range(len(array_for_checking)):
                if array_for_checking[i]!=".":
                    if int(array_for_checking[i])<=0 or int(array_for_checking[i])>=10:
                        return False
                    elif array_for_checking.count(array_for_checking[i])>1:
                        return False
            return True

        # row check
        for row in board:
            if not helper(row):
                return False

        # column check
        column_map = collections.defaultdict(int)
        for i in range(9):
            column_map[i] = []

        for row in range(9):
            for column in range(9):
                column_map[column].append(board[row][column])

        for column in column_map:
            if not helper(column_map[column]):
                return False

        # sub_box of 3x3 check
        sub_box_map = collections.defaultdict(int)
        for i in range(9):
            sub_box_map[i] = []

        for row in range(9):
            for column in range(9):
                sub_box_number = (column//3) + (3*(row//3))
                sub_box_map[sub_box_number].append(board[row][column])

        for sub_box in sub_box_map:
            if not helper(sub_box_map[sub_box]):
                return False
        return True

