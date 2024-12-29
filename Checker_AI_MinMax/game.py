# game.py

from checkers_logic import create_initial_board, get_legal_moves, apply_move, is_game_over
from ai_minimax import find_best_move

def print_board(board):
    """
    Simple console print of the board for debugging.
    """
    print("   ", " ".join(map(str, range(len(board)))))
    print("   " + "-" * (2 * len(board) - 1))
    for i, row in enumerate(board):
        print(i, "|", " ".join(["{:2d}".format(cell) for cell in row]))
def run_game():
    board = create_initial_board()
    current_player = 1  # 1 = black, -1 = white
    depth = 4
    
    move_count = 0
    max_moves = 150  # or any arbitrary limit

    while not is_game_over(board) and move_count < max_moves:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        moves = get_legal_moves(board, current_player)
        if not moves:
            print("No moves available!")
            break

        best_move = find_best_move(board, depth, current_player)
        if best_move is None:
            print("No possible move found. Game Over.")
            break
        
        # Debug: Print the move chosen
        print(f"AI Move #{move_count+1}: {best_move}")
        
        board = apply_move(board, best_move)
        current_player *= -1
        move_count += 1

    print_board(board)
    if move_count >= max_moves:
        print("Draw by move limit!")
    else:
        print("Game Over!")


if __name__ == "__main__":
    run_game()
