from reg import registration
from auth import authorization
def start_menu():
    while True:
        super().start_menu()
        start_menu().title('Авторизация/Регистрация')
        start_menu().geometry('1920x1080')
        start_input = input('If you first time here/want to enter to your account (R/A)')
        if start_input is "R":
            registration()
            break
        elif start_input is 'A':
            authorization()
            break
        else:
            print('Incorrect input, please try again')
