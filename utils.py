# utils.py
# Helper functions for reading and checking user input


def is_number(text):
    """Return True if text is made only of digits (0-9)."""
    if text == "":
        return False
    for ch in text:
        if ch not in "0123456789":
            return False
    return True


def get_int(prompt, low, high):
    """Keep asking until the user types a whole number from low to high."""
    while True:
        text = input(prompt).strip()
        if not is_number(text):
            print("Please enter digits only (no letters or symbols).")
        elif int(text) < low or int(text) > high:
            print("Please enter a number between", low, "and", high)
        else:
            return int(text)


def get_name(prompt):
    """Ask for a player name: 1 to 12 characters, not empty."""
    while True:
        name = input(prompt).strip()
        if len(name) == 0:
            print("Name cannot be empty.")
        elif len(name) > 12:
            print("Name must be 12 characters or fewer.")
        else:
            return name


def print_title(text):
    """Print a text banner between two lines."""
    line = "=" * 40
    print(line)
    print(text.center(40))
    print(line)


