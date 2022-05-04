

from random import randrange
N = 10
a = []
for _ in range(N):
    a.append(randrange(-10, 11))

f = "{:3d}" * N
print(f.format(*a))

max = -11
for i in range(N):
    if a[i] > max:
        max = a[i]
        imax = i
print(imax, max)


for i in range(imax):
    for j in range(i + 1, imax):
        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]
print(a)  

for i in range(imax, 11):
    for j in range( i + 1, 11):
        if a[i] < a[j]:
           a[j], a[i] = a[i], a[j]
print(a)  








