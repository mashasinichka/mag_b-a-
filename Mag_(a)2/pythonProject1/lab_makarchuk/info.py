from main_menu import*
from keyboard_folder import keyboard
import json
def vopros():
    while True:
        vopros = input("Вы хотите пройти полную регистрацию - ДА(R) / Нет (A)")
        if vopros is "A":
            main_menu()
        elif vopros is "R":
            info()

def info():
    print('\n Укажите дату рождения, почту, номер телефона')
    Birthd_input = input('Укажите дату рождения: ')
    email_input = input("Укажите почту: ")
    numb_input = input("Укажите номер телефона: ")
    user["Birthday"] = Birthd_input
    user["email"] = email_input
    user["number"] = numb_input
    data["users"].append(user)
    with open('user_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Информация успешно обновлена")
    if keyboard.wait('Enter'):
        print('Enter нажат!')
        main_menu()