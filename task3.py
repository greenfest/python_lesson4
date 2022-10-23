# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
from math import pi

n = int(input("Введите точность числа: "))
print(format(pi, f".{n}f"))

# Альтернативный вариант с библиотекой mpmath:

from mpmath import mp
def getPi(n):
   mp.dps=n+1
   return(mp.pi)

n = int(input("Введите точность числа: "))
print(getPi(n))   