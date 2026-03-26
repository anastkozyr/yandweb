from requests import get, post, delete

print(get('http://localhost:8010/api/v2/users').json())
print(get('http://localhost:8010/api/v2/users/2').json())
print(get('http://localhost:8010/api/v2/users/-1').json())  # нет пользователя
print(get('http://localhost:8010/api/v2/users/q').json())  # не число

print(post('http://localhost:8010/api/v2/users').json())  # нет словаря
print(post('http://localhost:8010/api/v2/users', json={'name': 'Ваня'}).json())  # не все поля
print(post('http://localhost:8010/api/v2/users', json={'name': 'Ваня', 'position': 'кок',
                                                       'surname': 'Иванов', 'age': 17, 'address': 'module_3',
                                                       'speciality': 'прог',
                                                       'hashed_password': '123', 'email': '123@mars.org'}).json())

print(delete('http://localhost:8010/api/v2/users/999').json())  # id = 999 нет в базе
print(delete('http://localhost:8010/api/v2/users/10').json())