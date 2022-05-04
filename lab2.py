# 1 zadacha
"""
print('''___
Это 1 задача''')

k = int(input("Введите K: "))
n = int(input("Введите N: "))
sum = 0

if k > n:   
    while n <= k:
        sum += n**2 # добавляем квадрат этого числа к сумме
        n += 1
    print(sum)
elif n > k:
    while k <= n:
        sum += k**2 # добавляем квадрат этого числа к сумме
        k += 1
    print(sum)
else: # если n = k
    sum += n**2
    print(sum)

# 2 zadacha

print('''___
Это 2 задача''')

n1 = int(input("ВВедите число N: "))
K = 0
for i in range(1, n1+1):
    n1 /= i
    if n1 < i+1:
        K = i
        break
print("Число K: " + str(K))
"""
# 3 zadacha
"""
print('''___
Это 3 задача''')

da = input("Построить таблицу умножения?: ")

if "да" or "Да" in da:
    print("Создаём")
    for i2 in range(1, 10):
        print('''_
Это умножение на ''' + str(i2))
        for i in range(1, 11):
            i *= i2
            print(str(int(i / i2)) + " * " + str(i2) + " = " + str(i) )
else:
    print("как хотите")
"""
# 4 zadacha
"""
print('''___
Это 4 задача''')

el20 = (input("Введите 20 симфолов английского языка: "))

while len(el20) != 20:
    print("Здесь не 20 символов")
    el20 = (input("Введите заново: "))
    continue
c = (input("Введите C элемент: "))
print(el20.count(c))
"""

# 5 zadacha
"""
print('''___
Это 5 задача''')

tens1 = []
for h in range(1, 11):
    tens = [int(input("Введите " + str(h) + " число: "))]
    tens1 += tens
tens1.sort()
print(tens1)
"""
# 8 zadacha
"""
print('''___
Это 8 задача''')

x1 = int(input("Введите X: "))
y1 = int(input("Введите Y: "))

while y1 <= 0 or x1 <= 0:
    print("Это не натуральное число")
    x1 = int(input("Введите X: "))
    y1 = int(input("Введите Y: "))
    continue
def multi(x, y):
    c = 0
    for ix in range(y):
        c += x
    print(c)
multi(x1, y1)
"""
# 9 zadacha
"""
print('''___
Это 9 задача''')

X = int(input("Введите двоичное число X: "))

def in10(a):
    a = str(a)
    k = 0
    for i in range(len(a)):
        k += int(a[i]) * (2 ** len(a) - i - 1)
    print(k)
in10(X)
"""
# 7 zadacha
"""
print('''___
Это 7 задача''')

x2 = float(input("Введите X: "))
y2 = float(input("Введите Y: "))

import math
pif = math.sqrt((x2**2) + (y2**2))

print("Расстояние от начала координат до точки: ", pif)
""" 
# 6 zadacha

print('''___
Это 6 задача''')


a = [
    [4, 5, 6, 9, 12],
    [7, 8, 9, 32, 12,],
    [10, 11, 12, 43, 76]
    [13, 61, 21, 32, 43,]
    [2, 95, 34, 56, 76,]
    ]
