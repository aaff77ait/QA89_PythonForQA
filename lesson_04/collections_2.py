fruits = ['zorange', 'strawberry', 'bango']

# sorted - FUNC - does not change the original list - returns new LIST
numbers = [12, 56, 94, 6]
print(max(numbers))
print(min(numbers))
res = sorted(numbers)
print(res) # [6, 12, 56, 94]
print(numbers) # [12, 56, 94, 6]
print(sorted(numbers, reverse=True)) # [94, 56, 12, 6]
print(sorted(fruits, reverse=True)) # ['zorange', 'strawberry', 'bango']
print(sorted(fruits)) # ['bango', 'strawberry', 'zorange']
print(sorted('python rules')) # [' ', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 's', 't', 'u', 'y']

word = 'pyThon'
print(sorted(word)) # ['T', 'h', 'n', 'o', 'p', 'y']
result= ''.join(sorted(word)) # Thnopy
print(result)

names = ['Alex', 'Kristina', 'Bob', 'Zhanna']
print(sorted(names)) # ['Alex', 'Bob', 'Kristina', 'Zhanna']
print(sorted(names, key=len)) # ['Bob', 'Alex', 'Zhanna', 'Kristina']

# sort - только для списка, меняет исходный список, но ничего не возвращает
# по алфавиту
names.sort()
print(names) # ['Alex', 'Bob', 'Kristina', 'Zhanna']
# по длинне
names.sort(key=len)
print(names) # ['Bob', 'Alex', 'Zhanna', 'Kristina']

