# math_quiz.py
# Module 2: the math quiz (uses the functions in algorithms.py)

import rng
import utils
import algorithms

TOPICS = ["GCD", "Prime", "Factorial", "Fibonacci", "Reverse", "Binary"]


def shuffle_topics(items):
    """Shuffle a list using our own random numbers (swap in place)."""
    for i in range(len(items) - 1, 0, -1):
        j = rng.rand_range(0, i)
        items[i], items[j] = items[j], items[i]
    return items


def ask_question(kind):
    """Ask one question of the given kind.
    Returns (is_correct, question_text, correct_answer)."""
    if kind == 0:
        g = rng.rand_range(2, 12)
        a = g * rng.rand_range(2, 9)
        b = g * rng.rand_range(2, 9)
        text = "What is the GCD of " + str(a) + " and " + str(b) + "?"
        correct = algorithms.gcd(a, b)
        print(text)
        answer = utils.get_int("Your answer: ", 1, 1000)

    elif kind == 1:
        n = rng.rand_range(2, 60)
        text = "Is " + str(n) + " a prime number?"
        if algorithms.is_prime(n):
            correct = 1
        else:
            correct = 2
        print(text)
        answer = utils.get_int("Your answer (1 = Yes, 2 = No): ", 1, 2)

    elif kind == 2:
        n = rng.rand_range(3, 7)
        text = "What is " + str(n) + "! (" + str(n) + " factorial)?"
        correct = algorithms.factorial(n)
        print(text)
        answer = utils.get_int("Your answer: ", 1, 100000)

    elif kind == 3:
        n = rng.rand_range(6, 15)
        text = "What is the Fibonacci number at position " + str(n) + "? (0, 1, 1, 2, ...)"
        correct = algorithms.fibonacci(n)
        print(text)
        answer = utils.get_int("Your answer: ", 0, 100000)

    elif kind == 4:
        n = rng.rand_range(100, 999)
        if n % 10 == 0:
            n = n + 1
        text = "What do you get when you reverse the digits of " + str(n) + "?"
        correct = algorithms.reverse_number(n)
        print(text)
        answer = utils.get_int("Your answer: ", 1, 100000)

    else:
        n = rng.rand_range(5, 63)
        text = "Convert " + str(n) + " to binary."
        correct = algorithms.to_base(n, 2)
        print(text)
        answer = input("Your answer: ").strip()

    return (answer == correct, text, correct)


def play(name):
    """Play one quiz round. Returns the score earned."""
    utils.print_title("MATH QUIZ")
    lucky = utils.get_int("Enter your lucky number (1-999): ", 1, 999)
    rng.set_seed(lucky)

    kinds = shuffle_topics([0, 1, 2, 3, 4, 5])
    score = 0
    streak = 0
    mistakes = []
    results = {}

    for number in range(len(kinds)):
        print()
        print("Question", number + 1, "of", len(kinds))
        is_correct, text, correct = ask_question(kinds[number])
        topic = TOPICS[kinds[number]]

        if is_correct:
            streak = streak + 1
            points = 10
            if streak > 1:
                points = points + 5 * (streak - 1)
            score = score + points
            results[topic] = "Right"
            print("Correct! +" + str(points), "points")
        else:
            streak = 0
            results[topic] = "Wrong"
            mistakes.append((text, correct))
            print("Not quite. The answer was", correct)

    print()
    print("Quiz finished,", name + ".")
    print("Topic results:")
    for topic in results:
        print(" ", topic, "-", results[topic])
    if len(mistakes) > 0:
        print("Review these:")
        for item in mistakes:
            print(" ", item[0], "->", item[1])
    print("Score earned:", score)
    return score


