from datetime import datetime

# 0 -> Empty cells
board = [
    [3, 0, 0, 0, 0, 9, 4, 0, 7],
    [0, 0, 0, 0, 0, 0, 8, 6, 0],
    [0, 0, 8, 1, 0, 4, 3, 0, 0],
    [0, 3, 1, 7, 0, 0, 0, 0, 0],
    [0, 9, 4, 0, 0, 0, 7, 8, 0],
    [0, 0, 0, 0, 0, 5, 1, 3, 0],
    [0, 0, 9, 5, 0, 3, 2, 0, 0],
    [0, 8, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 3, 6, 0, 0, 0, 0, 4],
]
empty_cell_list = []


def is_board_valid(row: int, column: int, value: int) -> bool:
    """
    Check if board is valid given row, column and particular value for that row x column
    """
    if value == 0:
        return False

    # Row and column control
    for i in range(9):
        if (i != column and board[row][i] == value) or (i != row and board[i][column] == value):
            return False

    # Sub-box control
    sub_box_i = 3 * (row // 3)
    sub_box_j = 3 * (column // 3)
    for i in range(sub_box_i, sub_box_i + 3):
        for j in range(sub_box_j, sub_box_j + 3):
            if i != row and j != column and board[i][j] == value:
                return False

    return True


def extract_empty_cells() -> None:
    """
    Extract initial empty cells and populate empty_cells list
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_cell_list.append((i, j))


def print_board() -> None:
    """
    Print board (Empty cells (0: int) will be replaced with space)
    """
    for i in range(9):
        line_str = "|"
        for j in range(9):
            line_str += " {} |".format(" " if board[i][j] == 0 else board[i][j])
        print(line_str)


def main() -> None:
    """
    Start solving process
    """
    start = datetime.utcnow()

    extract_empty_cells()
    print("Empty cell count: {}".format(len(empty_cell_list)))

    empty_cell_index = 0
    while True:
        row, column = empty_cell_list[empty_cell_index]
        value = board[row][column]

        while True:
            if value > 9:
                # Backtrack
                board[row][column] = 0
                empty_cell_index -= 1
                row, column = empty_cell_list[empty_cell_index]
                board[row][column] += 1
                break
            elif is_board_valid(row, column, value):
                # Continue
                board[row][column] = value
                empty_cell_index += 1
                break
            else:
                # Value is not appropriate for board, continue
                value += 1

        if empty_cell_index < 0:
            print("Invalid!")
            break
        elif empty_cell_index == len(empty_cell_list):
            print("Solved!")
            break

    print_board()

    # Calculate time interval
    end = datetime.utcnow()
    seconds = (end-start).total_seconds()
    print("Passed time: {:.3f} seconds".format(seconds))


if __name__ == "__main__":
    main()
