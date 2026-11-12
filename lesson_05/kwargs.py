# kwargs - Key Words Args
# ** - собирает все в словарь
def print_config(**kwargs):
    print(type(kwargs), kwargs)


print_config(browser='Chrome', headless=True, timeout=30)
# <class 'dict'> {'browser': 'Chrome', 'headless': True, 'timeout': 30}
print_config()


# <class 'dict'> {}

def create_user(**data):
    return data


user1 = create_user(name='John', email='mail.ru', password='123456')
print(user1)  # {'name': 'John', 'email': 'mail.ru', 'password': '123456'}


def example(a, b, c=10, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
example(1, 2, 3, 4, 5, 6, 7, name='Kristina')
# 1
# 2
# 3
# (4, 5, 6, 7) - кортеж - tuple
# {'name': 'Kristina'} - словарь -dict

