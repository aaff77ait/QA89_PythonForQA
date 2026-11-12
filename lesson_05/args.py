def total(*args):
    # * означает ВСЁ, то есть не знаем, сколько будет аргументов
    # * собирает все в tuple
    print(type(args), args)
    return sum(args)
print(total(1, 2, 3))
print(total(10, 20, 30))
print(total(1, 20))
print(total(10, 20, 30, 40, 50, 60, 70, 80, 90))
print(total())


# сначала идут позиционные, а затем *
def print_scores(students, *scores):
    print(f'Student: {students}')
    print(f'Scores: {scores}')
print_scores("Anna", 4, 4, 3, 2, 5)
print_scores("Bob", 4)
print('*' * 50)
def check_status_codes(*codes):
    for code in codes:
        assert code == 200
print(check_status_codes(200, 200, 200))
# print(check_status_codes(200, 404, 200)) # AssertionError