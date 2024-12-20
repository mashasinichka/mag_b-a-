print('26')
print()
print('задание 1')
from datetime import *
import time
date_time = time.strftime("%d.%m.%Y")
date_times = time.strftime("%d.%m.%y")
datin = time.strftime("%d %b %Y")
datins = time.strftime("%d %B %y")
dat = time.strftime("%d.%m.%y - день в году: %j, день недели: %A")
vremya = time.strftime("%H:%M:%S")
vremya1 = time.strftime("(%p): %H:%M:%S")
print(date_time)
print(date_times)
print(datin)
print(datins)
print(dat)
print('Точное время:', vremya)
print('Точное время', vremya1)
print()
print('задание 2')
current_time = time.localtime()
print('Сегодня:')
my_time = time.strftime("%a", current_time)
my_date = time.strftime("%b", current_time)
dante = time.strftime("%d.%m.%Y", current_time)
print(f"{my_time} {current_time.tm_mday} {my_date} {current_time.tm_year} {current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}")
print(dante)
print()
print('задание 3')
for i in range(1, 6):
    print(i)
    time.sleep(3)




