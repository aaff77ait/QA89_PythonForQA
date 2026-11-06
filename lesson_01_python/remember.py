age = 25
name = "John"
print(age)
print(name)

my_string = '''This is a multy-line string.
We've wrapped the text to the next line'''
print(my_string)

# экранирование
raw_string = r"C:\Program Files\Kristina\Python"
print(raw_string)
# r - все что идет после это строка

# класс type - позволяет определить тип данных
s1 = 'Hello World'
print(type(s1))  # <class 'str'>
s2 = 32
print(type(s2)) # <class 'int'>
s3 = True
print(type(s3)) # <class 'bool'>
s4 = 3.2
print(type(s4)) # <class 'float'>

s5 = 'Zeleno'
s6 = 'glazka'
s7 = s5 + s6 # Zelenoglazka
print(s7)

#  метод .join(список)
words = ["Hello", "World", "and", "Python"]
res = " ".join(words) # здесь внутри " ". указан сеператор
print(res)

st = 'ab' * 7
print(st) # ababababababab

st1 = 35 * '*'
print(st1)

s8 = 'alex fokin'
s9 = 'al'
if s9 in s8:
    print(f"Name '{s9}' is in '{s8}'")
else:
    print('No')

st = 'a'
if st == 'a' or st == 'b' or st == 'c' or st == 'd':
    print('Yes')
# ANOTHER WAY
if st in 'abcd':
    print('Yes')

# ***********************
# len()

ln = len('JDKFJ:J DLJSJ kjs lksjd  ') # 25
print(ln)
s1 = 'Zelenoglazka'
print(len(s1))

# для выделения символа используем индексацию
# есть строка ' P  Y  T  H  O  N '
# индекс      ' 0  1  2  3  4  5 '
# индекс      '-6 -5 -4 -3 -2 -1 '

st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])
# print(st[6]) - IndexError: string index out of range

print(st[-1]) # n

# ***********************
# my_string[start:end]
print(st[0:3]) # Pyt
print(st[2:5]) # tho
print(st[4:6]) # on

my_string = 'Hello World'
print(my_string[::2]) # HloWrd - если нет цифр, то включается вся строка
print(my_string[::-1]) # dlroW olleH

from_second = my_string[1::2]
print(from_second) # el ol

my_substring = my_string[1:10:3]
print(my_substring) # eoo

print(st[:1000000]) # Python
print("Result:", st[1000000:2]) # Result: ПУСТО, но не ошибка