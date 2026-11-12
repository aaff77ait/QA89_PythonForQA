# ========== Norm function
def greet(name):
    return f'Hello, {name}!'
result = greet('Jim')
print(result)

# result1 = greet()
# print(result1) # TypeError: greet() missing 1 required positional argument: 'name'


# ========== Default Parameters
# значение, которое подставить, если при вызове аргумент не передается

def create_user(name, role='user'): # параметры БЕЗ деф значений идут первыми
    return {
        'name': name,
        'role': role
    }
print(create_user('name'))  # {'name': 'name', 'role': 'user'}
print(create_user('name', 'admin'))  # {'name': 'name', 'role': 'admin'}


def calculate_discount(price, discount=10):
    return price - (price * discount / 100)
print(calculate_discount(100))  # 90.0

# параметры БЕЗ деф значений идут первыми, иначе ошибка:
# def foo(a=1, b):
#     return a + b
# print(foo(5)) # SyntaxError: parameter without a default follows parameter with a default

# def add_test_res(name, results=[]):
#     results.append(name)
#     return results
# print(add_test_res('Test Login')) # ['Test Login']
# print(add_test_res('Test LogOut')) # ['Test Login', 'Test LogOut'] - БАГ!!!
def add_test_res(name,results=None):
    if results is None:
        results = []
    results.append(name)
    # results.append(results)
    return results
print(add_test_res("test_login")) # ['test_login']
print(add_test_res("test_logout")) # ['test_logout']
# print(add_test_res("test_logout", "OK")) # AttributeError: 'str' object has no attribute 'append'

# ========= Позиционный вызов
def create_user1(username, email, role):
    return f"{username} {email} {role}"
print(create_user1("Kris", "email@gmail.com", "admin")) # Kris email@gmail.com admin
# ========= Именнованный вызов
print(create_user1(role='admin', username='alex',email='aaff77@mail.ru')) # alex aaff77@mail.ru admin
