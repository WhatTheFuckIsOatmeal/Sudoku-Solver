board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end="")

# finding an empty cell
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None

# find 3x3 subgrid segment and col/row for valid placement of num
def valid(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 Subgrid
    subgrid_x = pos[1] // 3  # Check horizontal subgrid
    subgrid_y = pos[0] // 3  # Check vertical subgrid

    start_row = subgrid_y * 3
    start_col = subgrid_x * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False  # If num is found in 3x3 subgrid, we have an invalid placement
    return True  # If num is not found in 3x3 subgrid, we have a valid placement
def solve(bo):
    empty = find_empty(bo)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True
            bo[row][col] = 0
    return False

if __name__ == "__main__":
    if solve(board):
        print_board(board)
    else:
        print("No solution available!")
