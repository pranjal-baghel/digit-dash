# main.py
# Digit Dash: starting point of the program (menu and overall flow)

import utils
import guessing_game
import math_quiz
import leaderboard


def show_menu(player):
    """Print the main menu."""
    utils.print_title("DIGIT DASH")
    print("Player:", player)
    print()
    print("1. Guessing Game")
    print("2. Math Quiz")
    print("3. Leaderboard")
    print("4. Statistics")
    print("5. Change Player")
    print("6. Exit")
    print()


def main():
    """Run the program until the player chooses Exit."""
    utils.print_title("WELCOME TO DIGIT DASH")
    player = utils.get_name("Enter your name: ")

    running = True
    while running:
        show_menu(player)
        choice = utils.get_int("Choose an option (1-6): ", 1, 6)
        print()

        if choice == 1:
            score = guessing_game.play(player)
            leaderboard.add_score(player, "Guessing Game", score)
        elif choice == 2:
            score = math_quiz.play(player)
            leaderboard.add_score(player, "Math Quiz", score)
        elif choice == 3:
            leaderboard.show_leaderboard()
        elif choice == 4:
            leaderboard.show_stats()
        elif choice == 5:
            player = utils.get_name("Enter the new player's name: ")
        else:
            print("Thanks for playing, " + player + "! Goodbye.")
            running = False

        if running:
            input("\nPress Enter to return to the menu...")
            print()


main()
