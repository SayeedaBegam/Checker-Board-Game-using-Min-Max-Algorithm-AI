# Checker-Board-Game-using-Min-Max-Algorithm-AI
his project is a Python-based Checkers (Draughts) game where:

You play as Black.
The AI (Minimax with alpha-beta pruning) controls White.
The game is visualized using Pygame, allowing you to click pieces and make moves on a standard 8×8 checkerboard.
Table of Contents
Features
Project Structure
Requirements
Installation
How to Run
Gameplay Instructions
Customization
Known Limitations
Future Improvements
License
Features
Graphical Board: Rendered with Pygame for an interactive experience.
Human vs. AI: Human controls the Black pieces, AI controls the White pieces.
Minimax Algorithm: Includes alpha-beta pruning for improved performance.
Mandatory Captures: If a capture is available, normal moves are not returned.
Automatic King Promotion: Pieces become kings upon reaching the opposite side.
Move Limit: By default, the game ends in a draw after a certain move limit (to avoid infinite loops).
Project Structure
arduino
Copy code
Checker_AI_MinMax/
├── ai_minimax.py
├── checkers_logic.py
├── pygame_ui.py
├── (optional) tests/
│    └── test_logic.py
└── README.md (this file)
checkers_logic.py

Contains core board creation and rules.
Move generation (including captures and multi-jumps).
Apply and promote piece logic.
Checks for game-over conditions.
ai_minimax.py

Simple evaluation function (piece count, king weighting).
Minimax function with alpha-beta pruning.
find_best_move helper for White (AI) or Black (if you ever do AI vs. AI).
pygame_ui.py

Visual interface with Pygame.
You (Black) can click on a black piece, then click on a valid diagonal square to move.
Computer (White) automatically moves using Minimax.
Basic loop that updates the board, checks for end-game, etc.
(optional) tests/ folder

Example unit tests with pytest or unittest to validate logic functions.
Requirements
Python 3.7+ (3.8+ recommended)
Pygame (2.x or above recommended)
Check your Python version:

bash
Copy code
python --version
If not installed, install Python from python.org or through your system’s package manager.

Installation
Clone or Download this repository:

bash
Copy code
git clone https://github.com/username/Checker_AI_MinMax.git
cd Checker_AI_MinMax
Install Dependencies:

bash
Copy code
pip install pygame
(Optionally, install testing tools if you want to run unit tests, e.g. pip install pytest.)

How to Run
From the Command Line (Terminal or PowerShell):
bash
Copy code
python pygame_ui.py
A new Pygame window should open, showing an 8×8 checkers board.
Gameplay Instructions
Human = Black, AI = White

Black pieces are dark circles, White pieces are blue circles.
Making a Move:

Click a black piece you want to move (only if it belongs to your side).
Click the valid diagonal square to move or capture.
If a capture is available (jump move), normal moves may be disabled (standard Checkers rule).
AI Turn:

After your move, White automatically decides its best move via Minimax and makes it.
Game End:

The game ends when either side has no moves left or when a predefined move limit is reached (draw).
Customization
Minimax Depth:

In pygame_ui.py, search for ai_depth = 4 and change to a higher or lower number.
Higher depth = stronger AI, but slower performance.
Lower depth = weaker AI, but faster moves.
Move Limit:

In pygame_ui.py, find max_moves = 200. Change as you like. If a game reaches this many moves, it’s called a draw.
Evaluation Function:

In ai_minimax.py, the function evaluate_board(board) uses a simple piece-count heuristic. You can refine this by considering board positioning, threatened pieces, etc.
Board Size:

Currently set to 8×8 in checkers_logic.py. Changing that to a different board dimension would require additional code changes (e.g., piece setup).
Known Limitations
No Draw by Repetition: The current code does not detect repeated board states. Instead, it uses a move limit to avoid infinite loops.
No Multiple Jump Highlight: The UI does not highlight subsequent forced jumps. You must click each jump in turn (though the code logic allows them).
Minimal User Feedback: The UI doesn’t show warnings for invalid moves. If you click an invalid square, nothing happens.
Future Improvements
Highlight Valid Moves: When a piece is selected, highlight all valid squares for clarity.
Draw by Repetition: Track board states to detect threefold repetition (or similar).
Transposition Tables: Speed up Minimax by caching visited board states.
Online Multiplayer: Allow human vs. human over the network.
Improved UI/UX: Add menus, animations, scoreboard, or piece animations.
License
(Choose a suitable license for your project—e.g., MIT License.)

python
Copy code
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
... (etc.)
Enjoy Playing and Hacking!
Feel free to submit issues or pull requests to help improve the project. Have fun playing Checkers against the Minimax AI!
