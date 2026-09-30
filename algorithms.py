# algorithms.py
# Basic algorithms used across the Digit Dash project


def gcd(a, b):
    """Greatest common divisor using Euclid's method."""
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def factorial(n):
    """Return n! (n factorial)."""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def fibonacci(n):
    """Return the nth Fibonacci number (0, 1, 1, 2, 3, 5, ...)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def reverse_number(n):
    """Reverse the digits of n, e.g. 123 becomes 321."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


def to_base(n, base):
    """Convert n to the given base (2 to 16) and return it as text."""
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n = n // base
    return result


# Quick check
print(gcd(12, 18))
print(is_prime(17))
print(factorial(5))
print(fibonacci(7))
print(reverse_number(123))
print(to_base(10, 2))
