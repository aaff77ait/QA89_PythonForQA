# append / insert
from lesson_04.tuple import my_tuple

fruits = ['orange', 'strawberry', 'mango']
fruits.append('orange')
print(fruits)  # ['orange', 'strawberry', 'mango', 'orange']

fruits.insert(1, 'banana')
print(fruits) # ['orange', 'banana', 'strawberry', 'mango', 'orange']

first_banana_index = fruits.index('banana')
print(f"The 'banana' was found at index {first_banana_index}") # The 'banana' was added to index 1

fruits.remove('orange') # ничего не возвращает
print(fruits) # ['banana', 'strawberry', 'mango', 'orange']

# рор - удаление элемента по индексу
fruits.pop(2)
print(fruits) # ['banana', 'strawberry', 'orange']

numbers = [10, 20, 30]
deleted = numbers.pop(1) # удали и верни то, что удалил
print(deleted) # 20
print(numbers) # [10, 30]
print(100 in numbers)

# можно удалить все элементы из списка и сделать список пустым
numbers.clear()
print(numbers) # []

