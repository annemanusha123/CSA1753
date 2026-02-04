N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row:
            return False
        if abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens(board, col):
    if col == N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            if solve_queens(board, col + 1):
                return True
    return False

def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

board = [-1] * N
solve_queens(board, 0)
print_board(board)
