# rng.py
# Our own pseudo-random number generator (through standard Linear Congruential Generator)

A = 1103515245
C = 12345
M = 2 ** 31

# The generator remembers its last number in this dictionary
state = {"seed": 12345}


def set_seed(value):
    """Choose the starting number (the seed)."""
    state["seed"] = value % M


def next_number():
    """Apply the formula once and return the new number."""
    state["seed"] = (A * state["seed"] + C) % M
    return state["seed"]


def rand_range(low, high):
    """Return a pseudo-random whole number from low to high (inclusive)."""
    size = high - low + 1
    return low + (next_number() // 65536) % size



