# 1 zadacha
"""
print('''
Это 1 задача
___''')
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
m = max(a, b, c)f
print("Максимальное число: " + str(m))

# 2 zadacha
print('''__
Это 2 задача''')
a1 = int(input("Введите первое число: "))
a2 = int(input("Введите второе число: "))
a3 = int(input("Введите третье число: "))
a4 = int(input("Введите четвертое число: "))
a5 = int(input("Введите пятое число: "))
nat = 0
if a1 > 0:
    nat += 1
if a2 > 0:
    nat += 1
if a3 > 0:
    nat += 1
if a4 > 0:
    nat += 1
if a5 > 0:
    nat += 1
print("Ответ:" + str(nat))

# 3 zadacha
print('''__
Это 3 задача''')
type1 = input("Введите элемент: ")
if type1.isdigit():
    print("Это цифра")
elif type1.isalpha():
    print("Это буква")
else:
    print("Это знаки препинания")

# 4 zadacha
print('''__
Это 4 задача''')
natur = float(input("Введите вещественнное число: "))

if natur > 0 and (int(natur) == natur):
    print("Да, это натуральное число")
else:
    print("Это не натуральное число")

# 5 zadacha
print('''__
Это 5 задача''')
a2 = int(input("Введите первое число: "))
b2 = int(input("Введите второе число: "))
c2 = int(input("Введите третье число: "))

if (a2 + b2) > c2 and (a2 + c2) > b2 and (c2 + b2) > a2:
    print("Да такой треугольник существует")
else:
    print("Такого треугольника не существует")
"""
# 6 zadacha
print('''__
Это 6 задача''')


gh = int(input("Введите число: "))

x = [int(a) for a in str(gh)]
if (x[0] + x[1] + x[2]) == (x[3] + x[4] + x[5]):
    print("Это число 'счастливый билетик'")
else:
    print("Это число не является 'счастливым билетиком'")

