"""
Final task #3
"""


def non_decr(num):
    return all(x <= y for x, y in zip(num, num[1:]))


def non_incr(num):
    return all(x >= y for x, y in zip(num, num[1:]))


def is_mono(num):
    return "true" if (non_decr(num) or non_incr(num)) else "false"


if __name__ == "__main__":
    print(is_mono([1, 1, 3, 4]))
