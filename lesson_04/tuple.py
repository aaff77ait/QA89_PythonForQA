# TUPLE - () - кортежи похожи на списки, но кортежи - НЕ изменяемый тип данных,
# и может содержать внутри другие списки

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 9)

my_tuple = ([1, 2, 3], ['a', 'b', 'c'])

first_element = numbers_tuple[1]
print(first_element)  # 2

first_element = my_tuple[1]
print(first_element)  # ['a', 'b', 'c']
print(first_element[1])  # b

nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[0])  # 1
print(nested_tuple[1])  # 2
print(nested_tuple[2])  # (3, 4)
print(nested_tuple[2][1])  # 4
print(nested_tuple[3])  # 5

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(tuple1 == tuple2)  # True
tuple3 = (1, 2, 4)
print(tuple1 == tuple3)  # False

# чтобы проверить "содержится ЛИ в кортеже" - in
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # True
print(100 in my_tuple)  # False
print(3 in nested_tuple)  # False (так как ВНУТРИ)

for el in my_tuple:
    print(el)
    # 1
    # 2
    # 3
    # 4
    # 5

i = 0
while i < len(my_tuple):
    print(my_tuple)
    i += 1
    # (1, 2, 3, 4, 5)
    # (1, 2, 3, 4, 5)
    # (1, 2, 3, 4, 5)
    # (1, 2, 3, 4, 5)
    # (1, 2, 3, 4, 5)

# DELETION
# del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
conc_tuple = tuple1 + tuple2
print(conc_tuple) # (1, 2, 3, 4, 5, 6)

# Длина
my_tuple = (1, 2, 3, 4, 5, (6, 7, 8))
print(my_tuple)
length_of_tuple = len(my_tuple)
print(length_of_tuple) # 6

# SUM
my_tuple = (1, 2, 3, 4, 5)
sum_of_tuple = sum(my_tuple)
print(sum_of_tuple) # 15

# MAX / MIN
max_of_tuple = max(my_tuple)
min_of_tuple = min(my_tuple)
print(max_of_tuple) # 5
print(min_of_tuple) # 1

my_tuple1 = ()
print(len(my_tuple1)) # 0
print(sum(my_tuple1)) # 0
# print(max(my_tuple1)) # ValueError: max() iterable argument is empty
# print(min(my_tuple1)) # ValueError: min() iterable argument is empty

original_tuple = (3, 1, 4, 5, 9, 6, 5, 5, 25, 3)
sorted_tuple = tuple((sorted(original_tuple)))
sorted_tuple_no_tuple = sorted(original_tuple)
print(original_tuple) # (3, 1, 4, 5, 9, 6, 5, 5, 25, 3) - кортеж
print(sorted_tuple) # (1, 3, 3, 4, 5, 5, 5, 6, 9, 25) - кортеж
print(sorted_tuple_no_tuple) # [1, 3, 3, 4, 5, 5, 5, 6, 9, 25] - список

# SLICES
sub_tuple = original_tuple[3:7]
print(sub_tuple) # (5, 9, 6, 5)

my_tuple_to_list = list(original_tuple)
print(my_tuple_to_list) # [3, 1, 4, 5, 9, 6, 5, 5, 25, 3]

my_string = ''.join(map(str, original_tuple))
print(my_string) # 31459655253
my_string = '   '.join(map(str, original_tuple))
print(my_string) # 3   1   4   5   9   6   5   5   25   3

my_tuple = (1, 2, 3, 4, 5)
my_tuple_to_list = list(my_tuple)
my_tuple_to_list[2] = 7777
updated_tuple = tuple(my_tuple_to_list)
print('my_tuple: ', my_tuple) # original tuple:  (1, 2, 3, 4, 5)
print('my_tuple_to_list: ', my_tuple_to_list) # my_tuple_to_list:  [1, 2, 7777, 4, 5]
print('updated_tuple: ', updated_tuple) # updated tuple:  (1, 2, 7777, 4, 5)