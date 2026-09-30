# Digit Dash

A menu driven and command line number arcade written in Python. It has a number guessing game, a math quiz built on classic algorithms, and a leaderboard with statistics.

**Author:** Pranjal Baghel, 26BCE10559
**Course:** Python Essentials (CSE1021 Introduction to Problem Solving and Programming), VIT Bhopal

## Overview

Digit Dash is a small game hub that runs entirely in the terminal. Player enters a name, then chooses between two games. Scores from every game are saved for the particular session and shown on a ranked leaderboard with statistics and information. The project applies the concepts like: functions, conditionals, loops, lists, tuples, sets, dictionaries, and classic algorithms such as GCD, prime numbers, Fibonacci, base conversion, and pseudo-random number generation.

## Features

- **Guessing Game:** three difficulty levels, hints (too high, too low, very close), a limited number of attempts based on the halving (binary search) idea, and a score that depends on speed and difficulty.
- **Math Quiz:** six questions in shuffled order covering GCD, prime numbers, factorial, Fibonacci, reversing digits, and binary conversion, with streak bonus points and a review of mistakes at the end.
- **Leaderboard:** ranks players by total score.
- **Statistics:** games played, number of players, average score, highest score, second best score, and players above average.
- **Random number generator:** built on a Linear Congruential Generator formula instead of a built-in random library.
- **Input validation:** invalid input (letters, out-of-range numbers, empty names) is rejected with a friendly message instead of crashing.

## Technologies Used

- Python 3 (developed and tested on Python 3.14)
- Python standard features only. No external libraries or installs are needed.
- Git and GitHub for version control

## Project Structure

```
digit-dash/
├── main.py            # program start, menu and overall flow
├── guessing_game.py   # Module 1: guessing game
├── math_quiz.py       # Module 2: math quiz
├── leaderboard.py     # Module 3: scores, ranking and statistics
├── algorithms.py      # GCD, prime, factorial, Fibonacci, reverse, base conversion
├── rng.py             # pseudo-random number generator (LCG)
├── utils.py           # input validation and display helpers
├── tests.py           # validation tests
├── statement.md       # problem statement
└── README.md          # this file
```

## How to Install and Run

1. **Install Python 3** from https://www.python.org/downloads/ if it is not already installed. Check with:
```
   python --version
```
2. **Download the project.** On the GitHub repository page, click **Code**, then **Download ZIP**, and extract it. (Or run `git clone https://github.com/pranjal-baghel/digit-dash.git`.)
3. **Open a terminal in the project folder.** In the extracted folder, click the address bar in File Explorer, type `cmd`, and press Enter.
4. **Run the program:**
```
   python main.py
```
5. Enter your name and follow the on-screen menu. No setup, configuration, or extra installation is required.

## How to Play

1. Choose **1** for the Guessing Game. Pick a level, enter a lucky number (it seeds the random generator), then guess the secret number.
2. Choose **2** for the Math Quiz. Answer six questions. Consecutive correct answers earn bonus points.
3. Choose **3** to view the leaderboard and **4** to view statistics.
4. Choose **5** to switch to another player, and **6** to exit.

Note: scores are kept in memory during a session and reset when the program closes.

## How to Test

Run the test file from the project folder:

```
python tests.py
```

It checks the algorithms, the random number generator, input validation, the game helpers, and the leaderboard, including edge cases such as an empty leaderboard and `factorial(0)`. Each check prints PASS or FAIL, and the last lines show `Tests failed: 0` and `All tests passed!` when everything works.

## Concepts Used

Syllabus topic - Where it is used
Functions, modules, parameters - every file
Tuple assignment - swapping values in `gcd`, shuffling and sorting 
Conditionals and loops (`if`, `while`, `for`, `break`, `continue`) - menus, games, validation 
Factorial, Fibonacci, reverse, base conversion - `algorithms.py` 
GCD, primes, pseudo-random numbers - `algorithms.py`, `rng.py` 
Efficiency of algorithms - halving idea in `guessing_game.py` 
Finding maximum, kth element, partitioning, counting - `leaderboard.py` 
Lists, tuples, sets, dictionaries - records, totals, unique players, levels 

## Future Enhancements

- Save scores to a file so they last between sessions.
- Add more games and question types.
- Add a two-player mode.
