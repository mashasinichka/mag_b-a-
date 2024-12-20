
print("13.1")

curr = {'1 - input': 'это оператор, который необходим для ввода определённой информации и последующих действий.',
        '2 - While': 'это функция, которой задаётся условие с последующим повторением до определённого момента, заданого в коде.',
        '3 - Переменная': '- средство для присваивания значений.',
        '4 - print': 'результат кода.',
        '5 - .join': 'этот мед в Python отвечает за объединение списка строк с помощью определенного указателя.',
        '6 - .keys': 'этот метод позволяет вывести ключи из словаря.',
        '7 - .items': 'этот метод позволяет ввести новые переменные в цикл "for" и вывести в каждую перменную ключ или же значение.',
        '8 - open': 'метод "open" отвечает за функцию открытия файла txt или иного для операций в коде.',
        '9 - import': 'данная функция может использоваться при написании кода, когда нужны необходимые функции из библиотеки.',
        '10 - for': 'эта функция отвечает за перебор в цикле переменных с последующими действиями, согласно коду.'}
for uiu in curr:
    print(f"{uiu} - {curr[uiu]}")

print("13.2")

reki = {'nile': 'egypt',
        'amazonka': 'Africa',
        'Ob': 'Russian and Kazahstan'}
for miu in reki:
    print(f"The {miu.title()} runs through {reki[miu].title()}.")

print("13.3")
#chisla_1 = (str(input()))
spisok = ['Thomas',
          'Lloyd',
          'Valentine',
          'Don']

slovar = {'Lillian',
          'Don',
          'William',
          'Cesari',
          'Valentine'}

for key in spisok:
    if key in slovar:
        print(f"{key} спасибо за пройденный опрос!")
    else:
        print(f"{key} пожалуйста, пройдите опрос.")

print("13.4")

slovar1 = {'Lillian',
          'Don',
          'William',
          'Cesari',
          'Valentine',
           'Valentine'}

for xi in set(slovar1):
    print(xi.title())

print("13.5")














