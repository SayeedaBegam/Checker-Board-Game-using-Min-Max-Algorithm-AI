# Checkers AI with Minimax

This project implements an interactive Checkers (Draughts) game in **Python**, where:
- **You** play as **Black** (human).
- **The AI** (using the **Minimax** algorithm with alpha-beta pruning) plays as **White**.
- A **Pygame** interface lets you click pieces and make moves on an 8×8 checkerboard.

---

## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [How to Run](#how-to-run)  
6. [Gameplay Instructions](#gameplay-instructions)  
7. [Customization](#customization)  
8. [Known Limitations](#known-limitations)  
9. [Future Improvements](#future-improvements)  
10. [License](#license)

---

## Features

- **Visual Board**: Displayed using **Pygame** for a 2D interactive experience.
- **Human vs. AI**: You control **Black**, while the computer (AI) controls **White**.
- **Minimax with Alpha-Beta Pruning**: Evaluates possible moves to find the best outcome for the AI.
- **Forced Captures**: If a capture is available, normal (non-capturing) moves become invalid.
- **Automatic King Promotion**: Pieces become kings upon reaching the opposite end of the board.
- **Move Limit**: To prevent games from going on indefinitely, a maximum move count can be set.

---

## Project Structure


1. **`checkers_logic.py`**  
   - Contains board creation, rules, move generation (including jumps), and functions to apply moves.

2. **`ai_minimax.py`**  
   - Provides the Minimax algorithm (with alpha-beta pruning), an evaluation function, and a helper to find the best move for a given player.

3. **`pygame_ui.py`**  
   - Sets up a Pygame window where you (Black) can click pieces to move, and the AI (White) makes its moves automatically.

4. **`tests/`** *(optional)*  
   - Sample tests using `pytest` or `unittest` to verify the correctness of the core logic.

---

## Requirements

- **Python 3.7+** (3.8+ recommended)
- **Pygame** (version 2.x or newer preferred)

Check your Python version:


## Git clone
git clone https://github.com/your-username/Checker_AI_MinMax.git
cd Checker_AI_MinMax
## Command to run
python pygame_ui.py
