print("задание 1")
for _ in range(3):
    my_fact = int(input())
    def factorial(my_fact):
        if my_fact == 1:
         return 1
        elif my_fact == 0:
            return 0
        else:
            return my_fact * factorial(my_fact - 1)
    print(factorial(my_fact))

print('задание 2')
for p in range(3):
    my_facti = int(input())
    def fibonacci(my_facti):
        if my_facti == 0:
            return 0
        elif my_facti == 1:
            return 1
        else:
            return fibonacci(my_facti - 1) + fibonacci(my_facti - 2)
    print(fibonacci(my_facti))

print('задание 3')
multiply = lambda x, y: x * y
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
product = multiply(num1, num2)
print("Произведение:", product)

print('задание 4')
prod = ['онил', 'ллойд', 'вячеслав', 'валентин', 'владимир', 'данил', 'николай', 'стас']
result = map(lambda x: x.upper(), prod)
print(list(result))


print('задание 5')
stroki = ['онил', 'ллойд', 'вячеслав', 'валентин', 'ян', 'ев', 'николай', 'стас']
strokii = list(filter(lambda stroki: len(stroki) > 3, stroki))
print(strokii)

print('задание 6')
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zipped = zip(list1, list2)
zipped_list = list(zipped)
print(zipped_list)

print('задание 7')
def pairwise_sum(lst1, lst2):
  if len(lst1) != len(lst2):
    print("Списки должны быть одинаковой длины")
  result = []
  for x, y in zip(lst1, lst2):
    result.append(x + y)
  return result
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
sum_list = pairwise_sum(lst1, lst2)
print(sum_list)

print('задание 8')
list_num_char = [('Lloyd', 1), ('William', 2), ('Tigran', 3), ('Den', 4), ('Lillian', 5)]
num_list, char_list = zip(*list_num_char)
print(num_list, char_list)