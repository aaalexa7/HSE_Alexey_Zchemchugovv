"""
Homework #13.2
"""
import json
import sys
from datetime import date

import requests
from bs4 import BeautifulSoup


def is_palindrome(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]


def predefined_sum(el_list, target):
    for idx, element in enumerate(el_list):
        if element < target:
            expected_pair_el = int(target) - int(element)
            expected_index = el_list.index(expected_pair_el)

            if expected_index > 0:
                print("Значение первого числа = %d значение второго = %d" % (element, expected_pair_el))
                print("Значение первого индекса = %d значение второго = %d" % (idx, expected_index))
                break


if __name__ == '__main__':
    print(is_palindrome("123321"))
    predefined_sum([2,7,11,15], 9)
