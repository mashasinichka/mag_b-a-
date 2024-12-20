print('#1')
x = int(input('Первое число: '))
s = int(input('Второе число: '))
while True:
    if s <= 10:
        print(x+s)
    else:
        print('wrong')
    break
print('#2')
print(eval(input()))
print('#3')
score = int(input('Введите число: '))
grade = ""
if score >= 80:
    grade = 'A'
    print(grade)
elif score >= 60:
    grade = "C"
    print (grade)
else:
    grade = "F"
    print (grade)





