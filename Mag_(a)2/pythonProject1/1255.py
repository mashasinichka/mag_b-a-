print('#1')
x = 10
def f():
    x = 5
    print(x)
f()
print(x)
print('#2')
y = 20
def outer():
    def inner():
        global y
        y += 2
    inner()
outer()
print(y)
print('#3')
z = 1
def modify():
    z = 2
    print(z)
    print(globals()['z'])
modify()
print('#4')
def check_built_in(zxc):
    lent = len(zxc)
    return lent
zxc = [1,2,3,4,5,6,7,8,9]
result = check_built_in(zxc)
print(result)
print('#5')
total = 100
def summa(ghoul):
    global total
    total -= sum(ghoul)
    return sum(ghoul)
ghoul = [1,2,3,4,5,6,7,8,9]
print(summa(ghoul))
print(total)
print("допы")
x = (input())
for i in range(-1,-170):
    if x in i:
        print(x)
        print('Принадлежит')
    else:
        print('Не принадлежит')











