
print("11.1")

spisok = ['admin', 'grisha', 'nikita', 'stas', 'dima']
for spisok1 in spisok:
    if spisok1 == 'admin':
        print("Hello admin, would you like to see a status report?.")
    else:
        print(f"Hello {spisok1}, thank you for logging in again.")
print("\nFinished making your pizza!")

print("11.2")

current_users = ['Stive', 'Oleg', 'Danya', 'Stas', 'Andrey']
new_users = ['Lloyd', 'Polina', 'Sonya', 'Lera', 'Takeshi']
for users in new_users:
    if users in current_users:
        print(f"{users} уже использовалось.")
    else:
        print(f"{users} не использовалось, выведите сообщние о его доступности.")

print('11.3')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chisla_1 = (int(input()))
for number in numbers:

    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = f"{number}th"
    print(ordinal)

print('15.1')

cars = (str(input("Какую машину хочешь взять на прокат? ")))
print(f"я хочу взять {cars} на прокат")

print('15.2')

mesta = (int(input("Сколько вы бы хотели взять мест? ")))
if mesta > 8:
    print("Подождите")
else:
    print("Стол готов")

print('15.3')

zapor = (int(input("Введите число: ")))
if zapor % 10 == 0:
    print("Число кратно 10")
else:
    print("Число не кратно 10")



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































