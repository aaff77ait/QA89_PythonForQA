with open('users.txt', 'w', encoding='utf-8') as f:
    f.write('Lora\n')
    f.write('Ivan\n')
    f.write('Коля\n')

# read() - читает все строки целиком
with open('users.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
# Lora
# Ivan
# Коля
print(len(content))
# 15 - включая три раза \n

print('*' * 20)
# readlines() - возвращает список
with open('users.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
# ['Lora\n', 'Ivan\n', 'Коля\n']
print(len(lines))
# 3
print(lines[2])
print('*' * 20)
with open('users.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print('!' * 20)
print('!' * 20)
# readline() - возвращает список строк
with open('users.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
print(line)
# Lora
print(len(line))
# 5
print(lines[2])
# Коля
print('==' * 20)

for line in lines:
    print(line.strip())
    print(line)
print('==' * 20)

#
