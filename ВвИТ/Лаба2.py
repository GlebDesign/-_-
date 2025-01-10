# def greet(n):
#     print('hello',n)
#
# def square(n):
#     print(n**2)
#
# def max_two(x, y):
#     if x>y:
#         print(x)
#     else:
#         print(y)
#
#
# def describe_person(name, age=30):
#     print('Имя', name, 'Возраст', age)
#
# def is_prime(x):
#     for i in range(2, x):
#         if x%i==0:
#             return False
#     return x>1
#
# is_prime(3)

#1. Two Sum
# def twosum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 print([i, j])
# twosum([3,2,4], 6)

def task2(l1, l2):
    a1 = ''
    for i in range(len(l1)):
        a1 += str(l1[i])
    a1 = int(a1)
    a2 = ''
    for j in range(len(l2)):
        a2 += str(l2[j])
    a2 = int(a2)
    a3 = a1 + a2
    res = []
    a3 = str(a3)
    for i in range(len(a3)):
        res.append(int(a3[i]))
    print(res[::-1])

task2([9,9,9,9,9,9,9], [9,9,9,9])
