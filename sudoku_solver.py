# Printing it in a neat way


def print_board(sudoku):
    for row in range(len(sudoku)):
        if row % 3 == 0 and row != 0:
            print("- "*15)
        for col in range(len(sudoku[0])):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            if col != 8:
                print(str(sudoku[row][col])+" ", end=" ")
            else:
                print(str(sudoku[row][col]))

# Returns the empty spaces in the Board


def empty_positions(sudoku):
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if sudoku[row][col] == 0:
                return (row, col)  # Same as (y,x)
    return None

# Ask input for inputting the numbers


def ask_input(board):
    sides = 9
    for row in range(sides):
        board.append([])
    for row in range(sides):
        for col in range(sides):
            num = int(input("Enter a number: "))
            board[row].append(num)
    return board


def solved(board):
    zeros = empty_positions(board)
    if not zeros:
        return True
    for i in range(1, 10):
        if is_valid(board, i, zeros):
            board[zeros[0]][zeros[1]] = i

            if solved(board) is True:
                return True
            else:
                board[zeros[0]][zeros[1]] = 0
    return False

# Trying if a certain position is valid


def is_valid(board, number, position):
    # Loop horzontally to make sure there is no same elts
    # i!=position to make sure it is not the new added element
    for i in range(len(board)):
        if number == board[position[0]][i] and i != position[1]:
            return False
        if number == board[i][position[1]] and i != position[0]:
            return False

    x_pos = (position[0]//3)*3
    y_pos = (position[1]//3)*3

    for i in range(3):
        for j in range(3):
            if number == board[x_pos+i][y_pos+j]:
                return False
    return True


# The hardest Sudoku ever Created
numbers = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]]

# Easy Example
# numbers = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]]


print_board(numbers)
print("\n")
solved(numbers)
if solved(numbers):
    print("Solved")
    print("\n")
    print_board(numbers)
else:
    print("Can't Solve it")
