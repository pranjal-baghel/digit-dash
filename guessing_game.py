# guessing_game.py
# Module 1: the number guessing game

import rng
import utils

# Difficulty levels: number -> (name, lowest, highest, score multiplier)
LEVELS = {
    1: ("Easy", 1, 50, 1),
    2: ("Medium", 1, 100, 2),
    3: ("Hard", 1, 500, 3),
}


def best_case_guesses(size):
    """Fewest guesses needed when always guessing the middle (halving idea)."""
    count = 0
    while size > 0:
        size = size // 2
        count += 1
    return count


def name_to_number(name):
    """Turn a name into a number by adding up its character codes."""
    total = 0
    for ch in name:
        total = total + ord(ch)
    return total


def choose_level():
    """Show the level menu and return the chosen level's details."""
    print("Choose a difficulty level:")
    for number in LEVELS:
        details = LEVELS[number]
        print(" ", number, "-", details[0], "(", details[1], "to", details[2], ")")
    choice = utils.get_int("Your choice: ", 1, 3)
    return LEVELS[choice]


def play(name):
    """Play one round. Returns the score earned (0 if the player loses)."""
    utils.print_title("GUESSING GAME")
    level_name, low, high, multiplier = choose_level()

    lucky = utils.get_int("Enter your lucky number (1-999): ", 1, 999)
    rng.set_seed(lucky * 31 + name_to_number(name))
    secret = rng.rand_range(low, high)

    best = best_case_guesses(high - low + 1)
    max_attempts = best + 3
    print()
    print("I am thinking of a number from", low, "to", high)
    print("You have", max_attempts, "attempts.")
    print("Tip: guessing the middle each time needs at most", best, "guesses!")

    guesses = []
    attempts = 0
    while attempts < max_attempts:
        guess = utils.get_int("Guess #" + str(attempts + 1) + ": ", low, high)
        if guess in guesses:
            print("You already tried that number. Try a new one.")
            continue
        guesses.append(guess)
        attempts = attempts + 1

        if guess == secret:
            remaining = max_attempts - attempts + 1
            score = remaining * 10 * multiplier
            print("Correct,", name, "! You got it in", attempts, "attempts.")
            print("Score earned:", score)
            return score

        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        if abs(guess - secret) <= (high - low) // 10:
            print("But you are very close!")

    print("Out of attempts. The number was", secret)
    print("Your guesses:", guesses)
    return 0



