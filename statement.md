# Problem Statement

## Problem
Practising basic programming concepts such as loops, functions, and data structures can feel dry and repetitive for beginners. Students like us often solve isolated exercises without seeing how these ideas combine into a complete program and they get very little instant feedback on how they are doing.

## Proposed Solution
Digit Dash is a command line arcade that turns these concepts into games. Student (Players) practise number reasoning and classic algorithms (GCD, primes, factorial, Fibonacci, reversing digits, base conversion) through a guessing game and a math quiz, and they can see their progress on a leaderboard.

## Scope
- Runs in the terminal on any computer with Python 3.
- Two games, a leaderboard, and statistics, all reachable from one menu.
- Multiple players can play in one session by switching the player name.
- Scores are stored in memory for the particular session only.
- Uses only basic and fundamental concepts and no external concepts.
- Not included: a graphical interface, online play, and saving data between sessions.

## Target Users
- First-year programming students who want practice that feels like a game.
- Teachers who want a simple demonstration project that combines many course concepts.
- Anyone learning basic algorithms.

## High-Level Features
1. Guessing Game with three difficulty levels, hints, and scoring.
2. Math Quiz with six algorithm-based questions, streak bonuses, and a review of mistakes.
3. Leaderboard ranking players by total score.
4. Statistics: games played, average, highest, and second best score, plus players above average.
5. Custom pseudo-random number generator built from a standard Linear Congruential Generator.
6. Input validation and friendly error messages throughout.
7. Automated validation tests in `tests.py`.
