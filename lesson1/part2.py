"""
Homework #2
"""


def list_and_dict():
    result = []
    for i in range(3):
        print(f'Введите через запятую для представителя {i + 1} имя, статус, ИНН')
        name, status, inn = str(input()).split(",")
        result.append({"name": name, "status": status, "INN": inn})
    print(result)


if __name__ == '__main__':
    list_and_dict()

