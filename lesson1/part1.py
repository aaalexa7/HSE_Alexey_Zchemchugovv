"""
Homework #1
"""


'''
1.	Поработайте с переменными, создайте несколько, выведите на экран. 
Запросите у пользователя некоторые числа и строки и сохраните в переменные, 
а затем выведите на экран. Используйте функции для консольного ввода input() и консольного вывода print(). 
Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов могут изменяться 
и сохранять за собой адрес в оперативной памяти.
'''


def variables():
    var_string = str(input())
    print(var_string)
    print(id(var_string))
    var_digit = int(input())
    print(var_digit)
    print(id(var_digit))


'''
2.	Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно в 
каждую переменную количество часов, минут и секунд. Переведите время в часы, минуты, секунды и 
сохраните в отдельных переменных.
Используйте приведение типов для перевода строк в числовые типы. Предусмотрите проверку 
строки на наличие только числовых данных через встроенный строковый метод .isdigit().
Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.
'''


def time_count():
    time_string = str(input())
    if not time_string.isdigit():
        raise Exception("Invalid input")
    hours = int(time_string) // 3600
    print("Hours: ", hours)
    minutes = int(time_string) % 3600 // 60
    print("Minutes: ", minutes)
    seconds = int(time_string) % 3600 % 60
    print("Seconds", seconds)


'''
3.	Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
Выведите данные в консоль.
'''


def digit_operations():
    digit = int(input())
    if digit > 9:
        raise Exception("Invalid input. Number should be in range 1-9")
    sum_diff_place_numbers = digit * 100 + digit * 10 + digit
    print(sum_diff_place_numbers)


if __name__ == '__main__':
    variables()
    time_count()
    digit_operations()

