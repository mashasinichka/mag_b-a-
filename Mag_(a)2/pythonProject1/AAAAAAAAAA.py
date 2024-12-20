
print("14.1")

user_0 = {'fist_name': 'Lloyd',
          'last_name': 'Austin',
          'age': '75',
          'city': 'Washington'}
user_1 = {'fist_name': 'Donald',
          'last_name': 'Trump',
          'age': '71',
          'city': 'Washington'}
user_2 = {'fist_name': 'Alexey',
          'last_name': 'Golovin',
          'age': '20',
          'city': 'Tyumen'}
people = [user_0, user_1, user_2]
for person in people:
    print(person['fist_name'], person['last_name'], person['age'], person['city'])

print("14.2")

print('Имя и любмое число:')
favourite_numbers = {'Илья': ['27','70','90'],
                     'Артур': ['27','70','15'],
                     'Стас': ['19','999','124124'],
                     'Никита': ['100','124'],
                     'Полина': ['18','7000']}

for absd, value in favourite_numbers.items():
    for number in value:
        print(f'{absd} - {number}')

print("14.3")

cities = {'Moscow': {'population': 'Примерно 25 миллионов человек.',
                     'country': 'Рооссия, столица Российской Федерации.',
                     'fact': 'Во время правления Пётром II, прозошёл перенос столицы из Санкт-петербурга в Москву, и до сих пор этот город является столицой Российской Федерации.'},
          'Saint-Petersburg': {'population': 'Примерно 7 миллионов человек.',
                               'country': 'Россия, Питер - самый населённый город на северо-западе Российской Федерации.',
                               'fact': 'Шведская интервенция в начале 18 века была проиграна Россией против Королевства Швеции.'},
          'Philadelphia': {'population': 'Около 6 миллионов человек.',
                         'country': 'Соединённые Штаты Америки, United States of America.',
                         'fact': 'Конституционный конвент был подписан в Филадельфии 4 июля 1776 года, благодаря этому США обрели статус: "Независимого государства".'}}

for city, city_info in cities.items():
    print(city)
    print(f"1) {city_info['country']}")
    print(f"2) {city_info['population']}")
    print(f"3) {city_info['fact']}")

print("16.1")

message = ""
while message != 'quit':
    message = (str(input("Введите дополнение для пиццы: ")))
    if message != 'выйти':
        print(f"Дополнение ({message}) включено в Ваш заказ. (для завершения, напиши: 'quit').")
print(f'Заказ завершен.')

print("16.2")

while True:
    age = (int(input("Введите ваш возраст (для выхода введите 0): ")))
    if age == 0:
        break
    elif age < 3:
        print("Билет бесплатный.")
    elif 3 <= age <= 12:
        print("Стоимость билета $10.")
    else:
        print("Стоимость билета $15.")

print("16.3")

mess = ''
while True:
    mess = (str(input("Введите дополнение для пиццы: ")))
    if mess == 'quit':
        break
    else:
        print(f"Дополнение ({mess}) включено в Ваш заказ.")


