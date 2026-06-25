# Tic-Tac-Toe AI

An AI-powered Tic-Tac-Toe game built with Python and Pygame. The project implements the Minimax algorithm to create an unbeatable AI opponent that always chooses the optimal move.

## Overview

This project explores the fundamentals of Artificial Intelligence through the classic game of Tic-Tac-Toe. The AI uses the Minimax algorithm, a decision-making algorithm commonly used in game theory and adversarial search problems, to evaluate all possible game states and determine the best move.

Because the AI considers every possible outcome, it plays optimally and cannot be defeated.

## Features

* Human vs AI gameplay
* Unbeatable AI powered by the Minimax algorithm
* Interactive graphical interface built with Pygame
* Optimal move selection through game tree search
* Win, lose, and draw detection
* Clean and intuitive user experience

## Technologies Used

* Python
* Pygame
* Minimax Algorithm
* Game Theory
* Adversarial Search

## How It Works

The AI evaluates every possible move and recursively explores future game states using the Minimax algorithm.

* **Maximizing Player (X):** Attempts to maximize the score.
* **Minimizing Player (O):** Attempts to minimize the score.
* The algorithm explores all possible outcomes and selects the move that leads to the best result.

This guarantees that the AI always makes the optimal decision.

## Installation

### Clone the repository

```bash
git clone https://github.com/1amchampion/Tictactoe-AI.git
cd Tictactoe-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install pygame
```

## Running the Project

```bash
python runner.py
```

## What I Learned

Through this project, I gained practical experience with:

* Artificial Intelligence fundamentals
* Recursive algorithms
* Adversarial search
* State-space exploration
* Game theory concepts
* Building graphical applications with Pygame

## Future Improvements

* Alpha-Beta Pruning for improved performance
* Difficulty levels
* Move visualization
* Game statistics and analytics
* Online multiplayer support

## License

This project is open-source and available under the MIT License.
