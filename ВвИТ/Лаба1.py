number=input('Введите число')
for i in range(1, int(number)+1):
    print(i)

a1=input('Введите первое число')
a2=input('Введите второе число')
if a1==a2:
    print('Error')
elif a1>a2:
    print(a1)
else:
    print(a2)