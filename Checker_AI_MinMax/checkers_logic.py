# checkers_logic.py

from copy import deepcopy

BOARD_SIZE = 8

# Representing pieces:
# 0  = empty
# 1  = black man
# 2  = black king
# -1 = white man
# -2 = white king

def create_initial_board():
    """
    Create a standard 8x8 checkers board layout.
    Black at the top rows, White at bottom rows.
    """
    board = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)]

    # Place black men in rows 0, 1, 2
    for row in range(3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = 1

    # Place white men in rows 5, 6, 7
    for row in range(5, 8):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 1:
                board[row][col] = -1

    return board

def in_bounds(r, c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def get_legal_moves(board, player):
    """
    Get all possible moves for 'player' (1 or -1).
    Each move is a dict:
      {
        'from': (start_r, start_c),
        'to': (end_r, end_c),
        'captures': [(cap_r, cap_c), ...]
      }
    """
    moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            piece = board[r][c]
            if piece != 0 and ((piece > 0 and player > 0) or (piece < 0 and player < 0)):
                piece_moves = get_piece_moves(board, r, c)
                moves.extend(piece_moves)

    # If any capture moves exist, return only captures (mandatory capture rule).
    capture_moves = [m for m in moves if m["captures"]]
    if capture_moves:
        return capture_moves
    return moves

def get_piece_moves(board, row, col):
    """
    Returns all possible moves for a single piece at (row, col).
    Includes normal moves and capturing (multi-jumps).
    """
    piece = board[row][col]
    moves = []

    # Determine directions
    if abs(piece) == 1:
        # man
        step = 1 if piece > 0 else -1
        directions = [(step, 1), (step, -1)]
    else:
        # king can move all 4 diagonals
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # First, check for captures
    capture_sequences = []
    visited_paths = []
    find_captures(board, row, col, piece, capture_sequences, visited_paths)

    if capture_sequences:
        moves.extend(capture_sequences)
    else:
        # No captures, check simple moves
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if in_bounds(nr, nc) and board[nr][nc] == 0:
                moves.append({
                    "from": (row, col),
                    "to": (nr, nc),
                    "captures": []
                })

    return moves

def find_captures(board, row, col, piece, results, visited_paths, current_path=None):
    """
    Recursively find all multi-jump capturing moves for a piece at (row, col).
    """
    if current_path is None:
        current_path = {
            "from": (row, col),
            "to": (row, col),
            "captures": []
        }

    directions = []
    if abs(piece) == 1:
        step = 1 if piece > 0 else -1
        directions = [(step, 1), (step, -1)]
    else:
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]

    found_capture = False

    for dr, dc in directions:
        mid_r = row + dr
        mid_c = col + dc
        jump_r = row + 2*dr
        jump_c = col + 2*dc

        if (in_bounds(mid_r, mid_c) and in_bounds(jump_r, jump_c)):
            if board[mid_r][mid_c] != 0 and (board[mid_r][mid_c]*piece < 0) and board[jump_r][jump_c] == 0:
                # valid capture
                temp_board = deepcopy(board)
                temp_piece = temp_board[row][col]
                temp_board[row][col] = 0
                temp_board[mid_r][mid_c] = 0
                temp_board[jump_r][jump_c] = temp_piece

                # check promotion
                temp_board = promote_if_needed(temp_board, jump_r, jump_c, temp_piece)

                new_path = {
                    "from": current_path["from"],
                    "to": (jump_r, jump_c),
                    "captures": current_path["captures"] + [(mid_r, mid_c)]
                }
                path_key = (row, col, jump_r, jump_c, tuple(new_path["captures"]))
                if path_key not in visited_paths:
                    visited_paths.append(path_key)
                    find_captures(temp_board, jump_r, jump_c, temp_piece, results, visited_paths, new_path)
                found_capture = True

    if not found_capture and len(current_path["captures"]) > 0:
        # store final path
        results.append(current_path)

def apply_move(board, move):
    """
    Applies the move to the board and returns a new board state.
    """
    from_r, from_c = move["from"]
    to_r, to_c = move["to"]
    new_board = deepcopy(board)
    piece = new_board[from_r][from_c]
    new_board[from_r][from_c] = 0

    # remove captured pieces
    for (cr, cc) in move["captures"]:
        new_board[cr][cc] = 0

    new_board[to_r][to_c] = piece
    # check promotion
    new_board = promote_if_needed(new_board, to_r, to_c, piece)
    return new_board

def promote_if_needed(board, row, col, piece):
    """
    Promotes a man to king if it reaches the last row for that color.
    """
    if piece > 0 and row == BOARD_SIZE - 1:
        board[row][col] = 2
    elif piece < 0 and row == 0:
        board[row][col] = -2
    return board

def is_game_over(board):
    """
    Game is over if either side has no moves.
    """
    black_moves = get_legal_moves(board, 1)
    white_moves = get_legal_moves(board, -1)
    if not black_moves or not white_moves:
        return True
    return False
