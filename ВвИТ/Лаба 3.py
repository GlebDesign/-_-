# 1
# with open('example.txt', 'r') as f:
#     txt=f.read()
#     print(txt)

# with open('example.txt', 'r') as f:
#     for i in f:
#         print(i)

# 2
# with open('user_input.txt', 'a') as f:
#     data=input('Введите текст:')
#     f.write(data)

# 3
try:
    with open('example.txt', 'r') as f:
        txt=f.read()
        print(txt)
except FileNotFoundError:
    print('Такого файла не существует')