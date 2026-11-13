# API

contact = {
    "id": 12,
    "name": "Anna",
    "email": "anna@gmail.com",
    "age": 18,

}

req_fields = {
    "id",
    "name",
    "email",
}

for field in req_fields:
    assert field in contact, f"In response field {field}"

"""
1. Написать функцию print_list_reverse(lst)
Функция принимает список и выводит этот список в консоль в обратном порядке.
Если lst равен None, пустой список, или если аргумент не является объектом типа list, функция должна вывести:
Wrong list
Пример:
print_list_reverse([1, 2, 3, 4, 5])
Вывод в консоль:
[5, 4, 3, 2, 1]
"""


def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
        return
    reversed_lst = lst[::-1]
    print(reversed_lst)


print_list_reverse([1, 2, 3, 4, 5])  # [5, 4, 3, 2, 1]
print_list_reverse([])  # Wrong list
print_list_reverse(None)  # Wrong list
print_list_reverse({1, 2, 3})  # Wrong list
print('=' * 50)

"""
2. Написать функцию is_valid_point(point)
Функция принимает кортеж и проверяет, является ли он корректной точкой на плоскости.
Условия корректной точки:
    • аргумент должен быть кортежем (tuple), а не списком или другим типом;
    • кортеж состоит ровно из 2 элементов;
    • оба элемента являются числами (int или float).
Если кортеж соответствует всем условиям, функция возвращает True.
Если аргумент не соответствует условиям, функция возвращает False.
Если point равен None или является пустым кортежем, функция возвращает None.
Примеры:
is_valid_point((3, 5))      # True
is_valid_point((3, "5"))    # False
is_valid_point([3, 5])      # False
is_valid_point((1, 2, 3))   # False
is_valid_point(())          # None
is_valid_point(None)        # None
"""


def is_valid_point(point):
    if point is None:
        return None
    if isinstance(point, tuple) and len(point) == 0:
        return None
    if not isinstance(point, tuple) or len(point) != 2:
        return False
    x, y = point
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return False
    return True


print(is_valid_point((3, 5)))  # True
print(is_valid_point((3, "5")))  # False
print(is_valid_point([3, 5]))  # False
print(is_valid_point((1, 2, 3)))  # False
print(is_valid_point(()))  # None
print(is_valid_point(None))  # None
print('=' * 50)

"""
3. Написать функцию print_sublist_reverse(lst, start, finish)
Функция принимает список, стартовый индекс и финишный индекс.
Нужно вывести в консоль список, в котором элементы от индекса start 
до индекса finish включительно расположены в обратном порядке, 
а остальные элементы остаются в обычном порядке.
Пример:
print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
Исходный список:
[10, 20, 30, 40, 50, 60]
Часть списка от индекса 1 до индекса 3 включительно:
[20, 30, 40]
После реверса:
[40, 30, 20]
Вывод в консоль:
[10, 40, 30, 20, 50, 60]
Если lst 
    равен None, 
    пустой список, 
    не является списком, 
    если start / finish не являются целыми числами, 
    если индексы start / finish выходят за пределы списка, 
    или start > finish, функция должна вывести:
Wrong args
Пример:
print_sublist_reverse([1, 2, 3], "0", 2)  # Wrong args (start не является целым числом)
"""


def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong args")
        return

    # Проверяем, что КАЖДЫЙ элемент списка является целым числом (int)
    for item in lst:
        if not isinstance(item, int):
            print("Wrong args")
            return

    if not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return

    if start < 0 or start >= len(lst) or finish >= len(lst) or start > finish:
        print("Wrong args")
        return

    beginning = lst[:start]
    middle_reverse = lst[start:finish + 1][::-1]
    end = lst[finish + 1:]
    print(beginning + middle_reverse + end)


# Проверка:
print_sublist_reverse([10, 20, 30, 40, '1', 60], 1, 3)  # Выведет: Wrong args
print_sublist_reverse([10, 20, 30, 40, 1, 60], 1, 3)  # Выведет: [10, 40, 30, 20, 1, 60]
print('=' * 50)

"""
4. Advanced — Написать функцию get_students_by_grade(students)
Функция принимает словарь, где ключ — имя студента, а значение — его оценка.
Нужно вернуть новый словарь, где ключ — оценка, а значение — список имён студентов, получивших эту оценку.
Пример:
get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
Результат:
{90: ["Alice", "Diana"], 85: ["Bob", "Charlie"]}
Если students равен None, является пустым словарём или аргумент не является словарём, функция должна вернуть пустой словарь:
{}
"""


def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students) == 0:
        return {}

    students_by_grade = {}

    for name, grade in students.items():
        # Если такой оценки еще нет в новом словаре, заводим для нее пустой список
        if grade not in students_by_grade:
            students_by_grade[grade] = []
        # Добавляем имя студента в список соответствующей оценки
        students_by_grade[grade].append(name)

    return students_by_grade


# Проверка:
print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
# Результат: {90: ['Alice', 'Diana'], 85: ['Bob', 'Charlie']}
