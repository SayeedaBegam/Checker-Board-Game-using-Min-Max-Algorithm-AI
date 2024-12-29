# pygame_ui.py

import pygame
import sys
from checkers_logic import (
    create_initial_board, get_legal_moves, apply_move, is_game_over
)
from ai_minimax import find_best_move

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (128, 128, 128)
RED   = (200, 0, 0)
BLUE  = (30, 144, 255)

BOARD_SIZE = 8
TILE_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * TILE_SIZE

pygame.init()
pygame.display.set_caption("Checkers with Minimax AI")
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

def draw_board(screen, board):
    """
    Draw squares and pieces on the Pygame screen.
    """
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            # Checkerboard coloring
            color = GRAY if (r + c) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))

            piece = board[r][c]
            if piece != 0:
                center_x = c*TILE_SIZE + TILE_SIZE//2
                center_y = r*TILE_SIZE + TILE_SIZE//2
                if piece > 0:
                    # Black piece
                    pygame.draw.circle(screen, BLACK, (center_x, center_y), TILE_SIZE//2 - 4)
                    if abs(piece) == 2:  # black king
                        pygame.draw.circle(screen, RED, (center_x, center_y), TILE_SIZE//4)
                else:
                    # White piece
                    pygame.draw.circle(screen, BLUE, (center_x, center_y), TILE_SIZE//2 - 4)
                    if abs(piece) == 2:  # white king
                        pygame.draw.circle(screen, RED, (center_x, center_y), TILE_SIZE//4)

def main():
    board = create_initial_board()
    current_player = 1  # 1 = black (human), -1 = white (AI)
    selected = None
    running = True
    ai_depth = 4  # Adjust as needed for performance

    # Limit how many total moves to avoid infinite games
    move_count = 0
    max_moves = 200

    clock = pygame.time.Clock()

    while running:
        screen.fill((0,0,0))
        draw_board(screen, board)
        pygame.display.flip()

        if is_game_over(board) or move_count >= max_moves:
            if move_count >= max_moves:
                print("Draw by move limit!")
            else:
                print("Game Over!")
            pygame.time.wait(3000)
            running = False
            continue

        if current_player == 1:
            # Human (Black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // TILE_SIZE, x // TILE_SIZE

                    # If nothing selected, try selecting a black piece
                    if selected is None:
                        if board[row][col] != 0 and board[row][col] * current_player > 0:
                            selected = (row, col)
                    else:
                        # Attempt to move the selected piece here
                        from_r, from_c = selected
                        valid_moves = get_legal_moves(board, current_player)
                        chosen_move = None
                        for m in valid_moves:
                            if m["from"] == (from_r, from_c) and m["to"] == (row, col):
                                chosen_move = m
                                break
                        if chosen_move:
                            board = apply_move(board, chosen_move)
                            current_player *= -1
                            move_count += 1
                        selected = None

            clock.tick(30)

        else:
            # AI (White)
            pygame.time.wait(500)  # Slight delay to see the board
            ai_move = find_best_move(board, ai_depth, current_player)
            if ai_move is None:
                running = False
            else:
                board = apply_move(board, ai_move)
            current_player *= -1
            move_count += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
