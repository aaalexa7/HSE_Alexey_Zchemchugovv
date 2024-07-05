"""
Homework #3
"""
from courts_data_array import courts
from parties_data_array import parties


def factorial():
    print('Введите n')
    n = int(input())
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    print(result)


def max_from_three():
    print('Введите через пробел три числа')
    result = list(map(int, input().split(" ")))
    print(max(result))


def area_of_rectangle():
    print('Введите через пробел два числа - длины катетов от прямого угла')
    first, second = list(map(int, input().split(" ")))
    print(first * second / 2)


def make_court_name(court):
    return court.replace('Арбитражного суда ', '')


def make_header(court, plaintiff, party):
    return f"В арбитражный суд {make_court_name(court['court_name'])}\n" \
           f"Адрес: {court['court_address']} \n\n" \
           f"Истец: {plaintiff['name']} \n" \
           f"ИНН {plaintiff['inn']}  ОГРНИП {plaintiff['ogrnip']} \n\n" \
           f"Ответчик: {party['full_name']} \n" \
           f"ИНН {party['inn']}  ОГРН {party['ogrn']} \n\n" \
           f"Адрес: {party['address']} \n" \
           f"Номер дела {party['case_number']} \n\n" \
           "--------------------------------------------------\n"


def calculate_header():
    plaintiff = {
        "name": "Иванов Иван Иванович",
        "inn": "1236182357",
        "ogrnip": "218431927812733",
        "address": "123534, г. Санкт-Петербург, пл. Дворцовая д.1"
    }
    for party in parties:
        court_code = party["case_number"].split("-")[0]
        court = courts[court_code]
        result = make_header(court, plaintiff, party)
        print(result)


if __name__ == '__main__':
    area_of_rectangle()

    factorial()
    max_from_three()
    area_of_rectangle()
    calculate_header()
