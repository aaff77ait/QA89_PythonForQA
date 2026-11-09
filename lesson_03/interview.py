"""
Написать функцию print_string_reverse(s)
Функция принимает строку и выводит эту строку в консоль в обратном порядке.
Если строка равна None, пустая или состоит только из пробелов, функция должна вывести:
Wrong string
Пример:
print_string_reverse("Shalom")
Вывод в консоль:
molahS
"""

def print_string_reverse(s):
    if s is None or s.strip() == "":
        print("Wrong string")
        return
    print(s[::-1])

print_string_reverse('123')
print_string_reverse(None)
print_string_reverse('')
print_string_reverse('   ')

"""
2. Написать функцию is_isr_phone_number(phone)
Функция принимает строку и проверяет, является ли она израильским номером телефона.
Условия корректного номера:
первая цифра — 0;
общее количество символов — 10;
все символы являются цифрами.
Если строка соответствует всем условиям, функция возвращает True.
Если строка не соответствует условиям, функция возвращает False.
Если строка равна None, пустая или состоит только из пробелов, функция возвращает None.
Примеры:
is_isr_phone_number("0521234567") → True
is_isr_phone_number("521234567") → False
is_isr_phone_number("05212345a7") → False
is_isr_phone_number("") → None
"""

def is_isr_phone_number(phone):
    if phone is None or phone.strip() == "":
        return None
    if len(phone) != 10:
        return False
    if phone[0] != "0":
        return False
    if not phone.isdigit():
        return False
    return True

phone_number = str(input("Enter phone number: "))

print(is_isr_phone_number(phone_number))


""""
3. Написать функцию print_substring_reverse(s, start, finish)
Функция принимает строку, стартовый индекс и финишный индекс.
Нужно вывести в консоль строку, в которой символы от индекса start до индекса finish 
включительно напечатаны в обратном порядке, а остальные символы остаются в обычном порядке.
Пример:
print_substring_reverse("Shalom", 1, 3)
Исходная строка:
Shalom
Часть строки от индекса 1 до индекса 3 включительно:
hal
После реверса:
lah
Вывод в консоль:
Slahom
Если строка равна None, пустая или состоит только из пробелов, или индексы 
start / finish выходят за пределы строки, или start > finish, функция должна вывести:
Wrong args
"""

def print_substring_reverse(s, start, finish):
    if s is None or s.strip() == "":
        print("Wrong args")
        return
    if start > finish or start < 0 or finish >= len(s):
        print("Wrong args")
        return
    beginning = s[:start]
    middle_reverse = s[start:finish+1][::-1]
    end_part = s[finish+1:]
    print(beginning + middle_reverse + end_part)

print_substring_reverse("Shalom", 1, 3)
print_substring_reverse(None, 1, 3)
print_substring_reverse("Shalom", 1, 10)
print_substring_reverse("Shalom", 3, 1)

"""
4. Advanced
Написать функцию get_words_reverse(s)
Функция принимает строку, где слова разделены пробелами, и возвращает исходную строку в обратном порядке слов.
Пример:
get_words_reverse("Hello my nice world")
Результат:
world nice my Hello
Advanced
Написать функцию print_words_reverse_in_column(s)
Функция принимает строку, где слова разделены пробелами, и выводит в консоль слова в столбик.
Каждое слово должно быть выведено задом наперед.
Пример:
print_words_reverse_in_column("Hello my nice world")
Вывод в консоль:
olleH
ym
ecin
dlrow
"""

def get_words_reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print(get_words_reverse("Hello my nice world"))

def print_words_reverse_in_column(s):
    words = s.split()
    for word in words:
        print(word[::-1])
print_words_reverse_in_column("Hello my nice world")