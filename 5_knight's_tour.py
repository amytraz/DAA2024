N = int(input("Enter Board size: "))
x = int(input("Starting row: "))
y = int(input("Starting col: "))

# Initialize the board with -1
board = [[-1 for i in range(N)] for i in range(N)]

def issafe(board, x, y):
    # Check if position is within bounds and not visited
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_board():
    # Print the board in a formatted way
    for i in range(N):
        for j in range(N):
            print(f"{board[i][j]:2}", end=" ")
        print()

def solvKTUtil(board, x, y, mov_x, mov_y, pos):
    # Base case: All squares are visited
    if pos == N**2:
        return True

    # Try all possible knight moves
    for i in range(8):
        new_x = x + mov_x[i]
        new_y = y + mov_y[i]

        if issafe(board, new_x, new_y):
            board[new_x][new_y] = pos
            if solvKTUtil(board, new_x, new_y, mov_x, mov_y, pos + 1):
                return True
            # Backtrack
            board[new_x][new_y] = -1

    return False

def solveKT():
    # All possible knight moves
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Set the starting position
    if not (0 <= x < N and 0 <= y < N):
        print("Starting position is out of bounds.")
        return

    board[x][y] = 0

    # Start the backtracking process
    if solvKTUtil(board, x, y, mov_x, mov_y, 1):
        print_board()
    else:
        print("Solution does not exist.")

solveKT()
