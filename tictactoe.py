import math

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Winning combinations: Rows, Columns, Diagonals
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [AI, AI, AI] in win_states:
        return 1  # AI Wins
    if [HUMAN, HUMAN, HUMAN] in win_states:
        return -1 # Human Wins
    return 0 # Draw or Ongoing

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    score = check_winner(board)
    
    # Terminal states: Win, Loss, or Draw
    if score == 1: return score
    if score == -1: return score
    if is_board_full(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = AI
                    score = minimax(board, depth + 1, False)
                    board[r][c] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[r][c] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                move_val = minimax(board, 0, False)
                board[r][c] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (r, c)
    return move

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to AI Tic-Tac-Toe! You are 'X'.")
    
    while True:
        print_board(board)
        
        # Human Turn
        try:
            row, col = map(int, input("Enter row and col (0-2) separated by space: ").split())
            if board[row][col] != EMPTY:
                print("Cell already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 0 and 2.")
            continue
            
        board[row][col] = HUMAN
        
        if check_winner(board) == -1:
            print_board(board)
            print("Wait... you won? (This shouldn't happen!)")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        # AI Turn
        print("\nAI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = AI
        
        if check_winner(board) == 1:
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()