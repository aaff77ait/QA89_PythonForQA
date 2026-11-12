# ===== Распаковка
# Есть готовый список / словарь, хотим разверунть при вызове

def login(username, password):
    print(username, password)

def login2(**kwargs):
    print(kwargs)

data = ['admin', '123456']
login(data[0], data[1]) # admin 123456
login(*data) # admin 123456

user = {
    'username': 'admin',
    'password': '123456'
}
login(**user) # admin 123456
login2(**user) # {'username': 'admin', 'password': '123456'}
