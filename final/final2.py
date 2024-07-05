"""
Final task #2
"""
const_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def to_int(to_convert: str) -> int:
    total_int = 0
    check_value = 0
    for i in range(len(to_convert)):
        current = const_values[to_convert[i]]
        if current > check_value:
            total_int += current - 2 * check_value
        else:
            total_int += current
        check_value = current
    return total_int


if __name__ == "__main__":
    print(to_int("LVIII"))
