def knights_tour(N, start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board[start_x][start_y] = 0

    def solve(x, y, move_count):
        if move_count == N * N:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == -1:
                board[nx][ny] = move_count
                if solve(nx, ny, move_count + 1):
                    return True
                board[nx][ny] = -1
        return False

    if solve(start_x, start_y, 1):
        for row in board:
            print(" ".join(str(cell).zfill(2) for cell in row))
        return True

    print("Solution does not exist")
    return False

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (N): "))
    start_x = int(input(f"Enter the starting X position (0 to {N-1}): "))
    start_y = int(input(f"Enter the starting Y position (0 to {N-1}): "))
    knights_tour(N, start_x, start_y)
