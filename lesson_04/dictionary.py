# DICT
books = {
    'Harry Potter and ...': 'J.K.Rowling',
    'To kill a mockingbird': 'Harper Lee',
}

books1 = {
    'Harry Potter and ...',
    'To kill a mockingbird',
}

print(books)
# {'Harry Potter and ...': 'J.K.Rowling', 'To kill a mockingbird': 'Harper Lee'}

print(books1)
# {'Harry Potter and ...', 'To kill a mockingbird'} - only keys

response = {
    'statusCode': 'success',
    'user': {
        'id': 1,
        'name': 'Kris'
    }
}

print(response['user']['name']) # Kris