# создание строк с шаблоном
print("=" * 60)
name = 'Alice'
age = 30
formatted_string = f"Hello, my name is {name} and I am {age} years old."
print(formatted_string)
print("=" * 60)

# метод find - принимает 3 аругмента - подстроку, индекс начала и индекс конца
s = 'AbrakadabraAbrakadabra'
str = 'bra'
print(s.find(str))  # вернет индекс ПЕРВОГО вхождения подсктроки, то есть 1
print(s.rfind(str))  # вернет индекс ПОСЛЕДНЕГО вхождения подсктроки, то есть 19
print(s.find('add'))  # вернет -1, так как не найдено
print("=" * 60)

# метод count(sub[cрока,начальный индекс,последний индекс]) - число повторений этой строки
print(s.count(str))  # вернет 4, так как в s содержится str всего 4 раза
print(s.count(str, 4))  # вернет 3, так как в s содержится str всего 3 раза начиная с индекса 4
print(s.count(str, 4, 16))  # вернет 2, так как в s содержится str всего 2 раза
# начиная с индекса 4 и до индекса 16 не включая
print("=" * 60)

# метод upper() - возвращает НОВУЮ строку в верхнем регистре / исходная не меняется
# метод lower() - возвращает НОВУЮ строку в НИЖНЕМ регистре / исходная не меняется
print(s.lower())  # вернет abrakadabraabrakadabra
print(s.upper())  # ABRAKADABRAABRAKADABRA
print(s)  # AbrakadabraAbrakadabra
print("=" * 60)

# Contact was added: j121hsl121khs12121ehfj4343fksj54545jfsjfs
# split() - разрезает строку по заданному делителю
s = 'Cat,Dog, Monster Rabbit, Pig'
print(s.split()) # по умолчанию делит по пробелу ['Cat,Dog,', 'Monster', 'Rabbit,', 'Pig']
print("-" * 30)
print(s.split(',')) # ['Cat', 'Dog', ' Monster Rabbit', ' Pig']
print("-" * 30)
print(s.split(',', 2)) # 2 это МАХ число разбиений по разделителю ['Cat', 'Dog', ' Monster Rabbit, Pig']
print("=" * 60)

# rjust() & ljust()
s = 'Hi!'
print(s.rjust(10, '*')) # *******Hi! - добавил указанных символов до 10 всего символов в строке
print("-" * 30)
print(s.ljust(10, '*')) # Hi!******* - добавил указанных символов до 10 всего символов в строке
print("=" * 60)
# EXAMPLE 1
test = ['Login', 'Cart', 'Api']
for t in test:
    print(t.ljust(15), 'OK')
# Login           OK
# Cart            OK
# Api             OK
print("-" * 30)
# EXAMPLE 2
order = '125'
print("Order Num.:", order.rjust(8, '0')) # Order Num.: 00000125
print("=" * 60)

# методы, которые позволяют определить из каких символов состоит строка
abc123 = 'abc123'
abc = 'abc'
one_two_three = '123'
xii = 'XII' # должно быть в ASCII-
flt = '4.23'
# nmbr = 4.23

print("-" * 30)
print("abc123 = ", abc123)
print("abc = ", abc)
print("123 = ", one_two_three)
print("-" * 30)
print("isalpha 'abc123' - ", abc123.isalpha())
print("isalnum 'abc123' - ", abc123.isalnum())
print("isnumeric 'abc123' - ", abc123.isnumeric())
print("isdigit 'abc123' - ", abc123.isdigit())
print("-" * 30)
print("isalpha 'abc - ", abc.isalpha())
print("isalnum 'abc' - ", abc.isalnum())
print("isnumeric 'abc' - ", abc.isnumeric())
print("isdigit 'abc' - ", abc.isdigit())
print("-" * 30)
print("isalpha '123' - ", one_two_three.isalpha())
print("isalnum '123' - ", one_two_three.isalnum())
print("isnumeric '123' - ", one_two_three.isnumeric())
print("isdigit '123' - ", one_two_three.isdigit())
print("-" * 30)
print("isalpha 'xii' - ", xii.isalpha())
print("isalnum 'xii' - ", xii.isalnum())
print("isnumeric 'xii' - ", xii.isnumeric())
print("isdigit 'xii' - ", xii.isdigit())
print("-" * 30)
print("isalpha 'flt' - ", flt.isalpha())
print("isalnum 'flt' - ", flt.isalnum())
print("isnumeric 'flt' - ", flt.isnumeric())  # проверяет на наличие только цифр от 0 - 9
print("isdigit 'flt' - ", flt.isdigit()) # проверяет на наличие только цифр от 0 - 9
print("-" * 30)
# print("isalpha 'nmbr' - ", nmbr.isalpha())
# print("isalnum 'nmbr' - ", nmbr.isalnum())
# print("isnumeric 'nmbr' - ", nmbr.isnumeric())
# print("isdigit 'nmbr' - ", nmbr.isdigit())

# INDEX
#index()
text = "QA automation with Python"
pos  = text.index("automation")
print(pos)

# replace
text1 = 'I like Python'
print(text1.replace('Python', 'Java')) # I like Java

text2 = '2026-07-03'
new_text = text2.replace('-', '/')
print(new_text) # 2026/07/03

