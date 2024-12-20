print('задание 22.1')
print()
for i in range(3):
    filename = 'learning_python'
    with open(filename) as file_object:
        contents = file_object.read()
    print(f"{contents}")
print()
print('задание 22.2')
print()

with open('learning_python') as file:
    content = file.read()
    content = content.replace("Python", "C++")
    print(content)









