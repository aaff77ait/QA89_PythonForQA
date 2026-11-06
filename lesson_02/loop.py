# =============================
# ===== ЦИКЛЫ / LOOPS =========
# =============================
# нужен для того, чтобы программа повторяла действие несколько раз
# FOR / WHILE

for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
for i in range(23, 26):
    print(i)
    # 23
    # 24
    # 25
for i in range(10, 20, 3):
    print(i)
    # 10
    # 13
    # 16
    # 19

# while выполняется хотя бы 1 раз всегда
x = 1
while x < 5:
    print(x)
    x += 1
    # 1
    # 2
    # 3
    # 4

str = 'Hi, loop!'
for c in str:
    if c == ',':
        print(c) # ,

str = 'Hi, loop!'
for c in str:
    if c == ',':
        break
    print(c)
    # H
    # i

str = 'Hi, loop!'
for c in str:
    if c == '***':
        break
    print(c)
    # H
    # i
    # ,
    #
    # l
    # o
    # o
    # p
    # !