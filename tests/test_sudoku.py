from board import Board
from examples import Examples, Solutions
from sudoku import Sudoku
from typing import List
import pytest


class TestSudoku:

    @pytest.mark.parametrize(
        "example_board, solution_board",
        [
            (Examples.EASIEST_1, Solutions.EASIEST_1), (Examples.EASIEST_2, Solutions.EASIEST_2), (Examples.INTERMEDIATE, Solutions.INTERMEDIATE),
            (Examples.DIFFICULT_1, Solutions.DIFFICULT_1), (Examples.DIFFICULT_2, Solutions.DIFFICULT_2), (Examples.NOT_FUN, Solutions.NOT_FUN),
            (Examples.UNSOLVABLE_1, Solutions.UNSOLVABLE_1), (Examples.UNSOLVABLE_2, Solutions.UNSOLVABLE_2), (Examples.UNSOLVABLE_3, Solutions.UNSOLVABLE_3),
            (Examples.UNSOLVABLE_4, Solutions.UNSOLVABLE_4), (Examples.UNSOLVABLE_5, Solutions.UNSOLVABLE_5), (Examples.UNSOLVABLE_6, Solutions.UNSOLVABLE_6),
            (Examples.UNSOLVABLE_7, Solutions.UNSOLVABLE_7), (Examples.UNSOLVABLE_8, Solutions.UNSOLVABLE_8), (Examples.UNSOLVABLE_9, Solutions.UNSOLVABLE_9),
            (Examples.UNSOLVABLE_10, Solutions.UNSOLVABLE_10), (Examples.UNSOLVABLE_11, Solutions.UNSOLVABLE_11)
        ]
    )
    def test_solve(self, example_board: List[List[int]], solution_board: List[List[int]]) -> None:
        """
        Testing solution
        """
        board = Board(example_board)
        Sudoku.solve(board)
        assert board.compare_boards(solution_board)
