from board import Board
from examples import Examples, Solutions
from sudoku import Sudoku
from typing import List
import pytest


class TestBoard:

    @pytest.mark.parametrize(
        "example_board, empty_cell_count",
        [
            (Examples.EASIEST_1, 45), (Examples.EASIEST_2, 45), (Examples.INTERMEDIATE, 57), (Examples.DIFFICULT_1, 58),
            (Examples.DIFFICULT_2, 47), (Examples.NOT_FUN, 62)
        ]
    )
    def test_empty_cells(self, example_board: List[List[int]], empty_cell_count: int) -> None:
        """
        Calculating empty cells
        """
        board = Board(example_board)
        empty_cell_list = board.extract_empty_cells()
        assert len(empty_cell_list) == empty_cell_count

    @pytest.mark.parametrize(
        "example_board, row, column, value, validity",
        [
            (Examples.EASIEST_1, 0, 0, 1, False), (Examples.EASIEST_1, 0, 0, 3, True), (Examples.EASIEST_1, 0, 2, 2, False),
            (Examples.INTERMEDIATE, 0, 8, 2, False), (Examples.INTERMEDIATE, 8, 8, 3, False), (Examples.INTERMEDIATE, 0, 6, 7, False),
            (Examples.DIFFICULT_1, 2, 2, 7, False), (Examples.DIFFICULT_1, 2, 2, 3, False), (Examples.DIFFICULT_1, 2, 0, 3, True),
        ]
    )
    def test_is_board_valid(self, example_board: List[List[int]], row: int, column: int, value: int, validity: bool) -> None:
        """
        Testing board validity
        """
        board = Board(example_board)
        assert validity == board.is_board_valid(row, column, value)

    @pytest.mark.parametrize(
        "example_board, solution_board",
        [
            (Examples.EASIEST_1, Solutions.EASIEST_1), (Examples.EASIEST_2, Solutions.EASIEST_2), (Examples.INTERMEDIATE, Solutions.INTERMEDIATE),
            (Examples.DIFFICULT_1, Solutions.DIFFICULT_1), (Examples.DIFFICULT_2, Solutions.DIFFICULT_2), (Examples.NOT_FUN, Solutions.NOT_FUN)
        ]
    )
    def test_solve(self, example_board: List[List[int]], solution_board: List[List[int]]) -> None:
        """
        Testing solution
        """
        board = Board(example_board)
        Sudoku.solve(board)
        assert board.compare_boards(solution_board)
