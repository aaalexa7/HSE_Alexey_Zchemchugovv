"""
Final task #1
"""


def fib(cnt):
    n, a, b = 0, 0, 1
    while a <= cnt:
        yield a
        a, b = b, a + b
        n = n + 1
    return a


if __name__ == "__main__":
    result = fib(10)
    print(list(result))
