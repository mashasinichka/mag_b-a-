print('17.1')
set1 = {1,3,5,7,9,11,13,15,17,19}
set2 = {2,4,6,8,10,12,14,16,18,20}
print(set1)
print(set2)
print('17.2')
set3 = set1.union(set2)
print(set3)
print('17.3')
set4 = {1,2,3,4,5,6,7,8,9,10}
set5 = {5,6,7,8,9,10,11,12,13,14,15}
set6 = set4.intersection(set5)
print(set6)
print('17.4')
set7 = {1,2,3,4,5,6,7,8,9,10}
set8 = {5,6,7,8,9,10,11,12,13,14,15}
set7 -= set8
print(set7)
print('17.5')
set9 = {1,2,3,4,5,6,7,8,9,10}
set10 = {5,6,7,8,9,10,11,12,13,14,15}
set11 = set9 ^ set10
print(set11)
print('17.6')
set12 = {1,2,2,3,3,4,5,6,7,8,9,10,10}
curr = (input('Введите число для добавления в множество: '))
while True:
    if curr in set12:
            print("данное число уже находится в множестве.")
    elif "exit" in curr:
        break
    else:
        set12.add(curr)
    print(set12)
    break
print('17.7')
set13 = {1,2,3,4,5,6,7,8,9,10}
set13.discard(5)
print(set13)
print('17.8')
lst = [1,2,5,6,8,10]
lst1 = [1,2,5,6,7,8,9,10,11,12,13,14,15]
lst_set = set(lst)
lst1_set = set(lst1)
set14 = set(lst) | set(lst1)
print(set14)
print('17.9')
my_list = [3,5,1,3,7,1,5,9]
my_list_set = set(my_list)
unique_set = set(my_list)
unique_list = sorted(list(unique_set))
print(unique_list)
print('17.10')
set15 = {1,2,3,4,5}
set16 = {1,2,3,4,5,6,7,8,9,10}
print(set15.intersection(set16))










































