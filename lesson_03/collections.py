fruits = ['orange', 'strawberry', 'mango']
empty_list = []
mixed_list = [2, 'orange', 4.22, True]

# операции со списками
fruits = ['orange', 'strawberry', 'mango']
print(fruits[0]) # orange
print(fruits[-1]) # mango
print(fruits[-2]) # strawberry
print(fruits[-3]) # orange
# print(fruits[-4]) # ERROR

fruits[1] = 'lemon'
print(fruits) # ['orange', 'lemon', 'mango']

# Concatenation
list1 = ['orange', 'lemon']
list2 = ['shampoo', 'soap']
combined_list = list1 + list2
print(combined_list) # ['orange', 'lemon', 'shampoo', 'soap']

# разложить список на переменные
fruits = ['orange', 'strawberry', 'mango']
first, second, third = fruits
print(first)
print(second)
print(third)

# разложить список на переменные - разное количество
fruits = ['orange', 'strawberry', 'mango', 'apple']
first, second, *rest = fruits
print(first) # orange
print(second) # strawberry
print(rest) # ['mango', 'apple']

# распаковка
fruits = ['orange', 'strawberry', 'mango']
for item in fruits:
    print(f"item in fruits: {item}")
    # item in fruits: orange
    # item in fruits: strawberry
    # item in fruits: mango

# comparison
correct_answers = ['orange', 'strawberry', 'mango']
user_answers = ['orange', 's', 'zuuuuuuuuungo']
if correct_answers == user_answers: # проверка по длине и содержанию
    print("All answers are correct")
else:
    print("Some answers are incorrect")

print(len(user_answers)) # 3
# max(user_answers)
numbers = [12, 56, 95, 6]
print("Word that starts from the HIGHEST letter:", max(user_answers)) # MAX word: s
print("Word that starts from the LOWEST letter:", min(user_answers)) # MIN word: orange
print("Length of the  word:", len(min(user_answers))) # MIN word: 6

print("MAX num:", max(numbers)) # 95
print("MIN num:", min(numbers)) # 6