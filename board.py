from typing import List, Tuple


class Board:
    def __init__(self, board):
        self._board = board
        self.extract_empty_cells()

    def extract_empty_cells(self) -> List[Tuple[int, int]]:
        """
        Extract initial empty cells and populate empty_cells list
        """
        empty_cell_list = []
        for i in range(9):
            for j in range(9):
                if self._board[i][j] == 0:
                    empty_cell_list.append((i, j))
        return empty_cell_list

    def is_board_valid(self, row: int, column: int, value: int) -> bool:
        """
        Check if board is valid given row, column and particular value for that row x column
        """
        if value == 0:
            return False

        # Row and column control
        for i in range(9):
            if (i != column and self._board[row][i] == value) or (i != row and self._board[i][column] == value):
                return False

        # Sub-box control
        sub_box_i = 3 * (row // 3)
        sub_box_j = 3 * (column // 3)
        for i in range(sub_box_i, sub_box_i + 3):
            for j in range(sub_box_j, sub_box_j + 3):
                if i != row and j != column and self._board[i][j] == value:
                    return False

        return True

    def print_board(self) -> None:
        """
        Print board -> Empty cells (0: int) will be replaced with space
        """
        for i in range(9):
            line_str = "|"
            for j in range(9):
                line_str += " {} |".format(" " if self._board[i][j] == 0 else self._board[i][j])
            print(line_str)

    def set_value(self, row: int, column: int, value: int) -> None:
        """
        Set given value in board with respect to rox x column position
        """
        self._board[row][column] = value

    def increment_value(self, row: int, column: int) -> None:
        """
        Increment value in row x column position
        """
        self._board[row][column] += 1

