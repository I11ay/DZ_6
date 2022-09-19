#                        Классаная работа
# Первое задание:

c = int(input())
N = int(input())
b = 0
while c != N:
    c += 1
    b += c
    print(b)

# Второе задание:

A = int(input())
B = int(input())
c = 0
while A < B:
    A += 1
    if A % 2 == 0:
        c += A
        print(c)

# Третье Задание:


A = int(input())
B = int(input())
c = 0
while c != A:
    while c != B:
        c += 1
        print("*" * A)
    exit()

# Четвертое задание:

N = int(input())
c = 0
while c < N:
    N -= 1
    print("*" * N)

#                       Домашняя работа
# Первое задание:

N = int(input())
c = 0

while c != N:
    N -= 1
    print("*" * N)

# Второе задание:

N = int(input())
c = 0
while c != N:
    c += 1
    print("*" * c)

# Третье Задание:

N = int(input())
c = 0
b = -1
while c != N:
    N -= 1
    b += 1
    print(" " * b + N * "*")

# Четвертое задание:

N = int(input())
c = 0
b = N
while c != N:
    c += 1
    b -= 1
    print(" " * b + c * "*")
