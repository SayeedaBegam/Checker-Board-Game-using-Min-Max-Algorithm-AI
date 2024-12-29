# ai_minimax.py

import math
from checkers_logic import get_legal_moves, apply_move, is_game_over

def evaluate_board(board):
    """
    A simple evaluation:
      Score = (# black men + 2 * # black kings) - (# white men + 2 * # white kings).
    """
    black_score = 0
    white_score = 0
    for row in board:
        for cell in row:
            if cell == 1:   # black man
                black_score += 1
            elif cell == 2: # black king
                black_score += 2
            elif cell == -1:  # white man
                white_score += 1
            elif cell == -2:  # white king
                white_score += 2
    return black_score - white_score

def minimax(board, depth, alpha, beta, maximizing):
    """
    Minimax with alpha-beta pruning.
    """
    if depth == 0 or is_game_over(board):
        return evaluate_board(board)

    if maximizing:
        max_eval = -math.inf
        moves = get_legal_moves(board, 1)  # black moves
        if not moves:
            return evaluate_board(board)
        for move in moves:
            new_board = apply_move(board, move)
            eval_val = minimax(new_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        moves = get_legal_moves(board, -1)  # white moves
        if not moves:
            return evaluate_board(board)
        for move in moves:
            new_board = apply_move(board, move)
            eval_val = minimax(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board, depth, player):
    """
    Returns the best move for 'player' (1 = black, -1 = white) using Minimax.
    """
    moves = get_legal_moves(board, player)
    if not moves:
        return None

    best_move = None
    if player == 1:
        # maximizing
        best_eval = -math.inf
        for move in moves:
            new_board = apply_move(board, move)
            eval_val = minimax(new_board, depth - 1, -math.inf, math.inf, False)
            if eval_val > best_eval:
                best_eval = eval_val
                best_move = move
    else:
        # minimizing
        best_eval = math.inf
        for move in moves:
            new_board = apply_move(board, move)
            eval_val = minimax(new_board, depth - 1, -math.inf, math.inf, True)
            if eval_val < best_eval:
                best_eval = eval_val
                best_move = move

    return best_move
