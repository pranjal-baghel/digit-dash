# tests.py
# Simple validation tests for Digit Dash.
# Run this file to check that the important functions give correct answers.

import algorithms
import rng
import utils
import leaderboard
import guessing_game
import math_quiz

passed = 0
failed = 0


def check(description, actual, expected):
    """Compare actual and expected values and print PASS or FAIL."""
    global passed, failed
    if actual == expected:
        passed = passed + 1
        print("PASS:", description)
    else:
        failed = failed + 1
        print("FAIL:", description, "| expected", expected, "but got", actual)


# ---------- algorithms.py ----------
print("--- Testing algorithms ---")
check("gcd(12, 18)", algorithms.gcd(12, 18), 6)
check("gcd(17, 5) coprime", algorithms.gcd(17, 5), 1)
check("gcd(7, 0)", algorithms.gcd(7, 0), 7)
check("is_prime(2)", algorithms.is_prime(2), True)
check("is_prime(97)", algorithms.is_prime(97), True)
check("is_prime(15)", algorithms.is_prime(15), False)
check("is_prime(1)", algorithms.is_prime(1), False)
check("is_prime(0)", algorithms.is_prime(0), False)
check("factorial(0)", algorithms.factorial(0), 1)
check("factorial(5)", algorithms.factorial(5), 120)
check("fibonacci(0)", algorithms.fibonacci(0), 0)
check("fibonacci(1)", algorithms.fibonacci(1), 1)
check("fibonacci(10)", algorithms.fibonacci(10), 55)
check("reverse_number(123)", algorithms.reverse_number(123), 321)
check("reverse_number(1000)", algorithms.reverse_number(1000), 1)
check("to_base(10, 2)", algorithms.to_base(10, 2), "1010")
check("to_base(255, 16)", algorithms.to_base(255, 16), "FF")
check("to_base(0, 2)", algorithms.to_base(0, 2), "0")

# ---------- rng.py ----------
print("--- Testing random number generator ---")
rng.set_seed(42)
first_run = []
for _ in range(5):
    first_run.append(rng.rand_range(1, 100))
rng.set_seed(42)
second_run = []
for _ in range(5):
    second_run.append(rng.rand_range(1, 100))
check("same seed gives same sequence", first_run, second_run)

in_range = True
rng.set_seed(7)
for _ in range(200):
    value = rng.rand_range(10, 20)
    if value < 10 or value > 20:
        in_range = False
check("200 numbers stay inside 10 to 20", in_range, True)

# ---------- utils.py ----------
print("--- Testing input validation ---")
check("is_number('123')", utils.is_number("123"), True)
check("is_number('12a')", utils.is_number("12a"), False)
check("is_number('') empty text", utils.is_number(""), False)
check("is_number('-5') negative sign", utils.is_number("-5"), False)

# ---------- guessing_game.py ----------
print("--- Testing guessing game helpers ---")
check("best_case_guesses(100)", guessing_game.best_case_guesses(100), 7)
check("best_case_guesses(50)", guessing_game.best_case_guesses(50), 6)
check("name_to_number('ab')", guessing_game.name_to_number("ab"), 195)

# ---------- math_quiz.py ----------
print("--- Testing quiz helpers ---")
shuffled = math_quiz.shuffle_topics([0, 1, 2, 3, 4, 5])
has_all = True
for i in range(6):
    if i not in shuffled:
        has_all = False
check("shuffle keeps all 6 topics", has_all and len(shuffled) == 6, True)

# ---------- leaderboard.py ----------
print("--- Testing leaderboard ---")
leaderboard.records.clear()
check("average of empty leaderboard", leaderboard.average_score(), 0)
check("highest score of empty leaderboard", leaderboard.highest_score(), None)

leaderboard.add_score("Asha", "Guessing Game", 60)
leaderboard.add_score("Ravi", "Math Quiz", 45)
leaderboard.add_score("Asha", "Math Quiz", 30)
leaderboard.add_score("Meena", "Guessing Game", 80)
leaderboard.add_score("Ravi", "Guessing Game", 20)

totals = leaderboard.player_totals()
check("player totals", totals, {"Asha": 90, "Ravi": 65, "Meena": 80})
ranked = leaderboard.sort_descending(list(totals.items()))
check("top ranked player", ranked[0], ("Asha", 90))
check("last ranked player", ranked[2], ("Ravi", 65))
check("highest score", leaderboard.highest_score(),
      ("Meena", "Guessing Game", 80))
check("average score", leaderboard.average_score(), 47.0)
check("best score (k=1)", leaderboard.kth_best_score(1), 80)
check("second best score (k=2)", leaderboard.kth_best_score(2), 60)
check("k too big gives None", leaderboard.kth_best_score(6), None)
check("unique players", leaderboard.unique_players(),
      {"Asha", "Ravi", "Meena"})
check("games count", leaderboard.games_count(),
      {"Guessing Game": 3, "Math Quiz": 2})
above, rest = leaderboard.split_by_average(totals)
check("above average players", above, ["Asha", "Meena"])
check("other players", rest, ["Ravi"])

# Clean up so the tests leave no fake scores behind
leaderboard.records.clear()

# ---------- summary ----------
print()
print("Tests passed:", passed)
print("Tests failed:", failed)
if failed == 0:
    print("All tests passed!")
else:
    print("Some tests failed. Check the FAIL lines above.")
