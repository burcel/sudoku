from board import Board
from datetime import datetime
from examples import Examples


class Sudoku:

    def __init__(self):
        pass

    @staticmethod
    def solve(board: Board) -> None:
        """
        Solve given board and update it with the result
        """
        empty_cell_list = board.extract_empty_cells()
        print("Empty cell count: {}".format(len(empty_cell_list)))

        from_backtrack = False
        empty_cell_index = 0
        while True:
            if empty_cell_index < 0:
                print("Invalid!")
                break
            elif empty_cell_index == len(empty_cell_list):
                print("Solved!")
                break
            else:
                row, column = empty_cell_list[empty_cell_index]
                value = board.get_value(row, column)
                if from_backtrack is True:
                    value += 1
                    from_backtrack = False
                while True:
                    if value > 9:
                        # -- Backtrack --
                        # Set current value to 0
                        board.set_value(row, column, 0)
                        # Reverse index by 1
                        empty_cell_index -= 1
                        # Increment previous value
                        from_backtrack = True
                        break
                    elif board.is_board_valid(row, column, value):
                        # -- Continue to next cell --
                        board.set_value(row, column, value)
                        empty_cell_index += 1
                        break
                    else:
                        # -- Continue to next value --
                        value += 1

            # print("--")
            # board.print_board()
            # input("?")


def main() -> None:
    start = datetime.utcnow()

    board = Board(Examples.NOT_FUN)
    Sudoku.solve(board)
    board.print_board()

    # Calculate time interval
    end = datetime.utcnow()
    seconds = (end - start).total_seconds()
    print("Passed time: {:.3f} seconds".format(seconds))


if __name__ == "__main__":
    main()
