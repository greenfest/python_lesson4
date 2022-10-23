# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5
import math

def primeFactors(n):
   i = 2
   primeList = []
   while i * i <= n:
       while n % i == 0:
           primeList.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primeList.append(math.floor(n))
   return primeList

n = int(input("Введите число N: "))
print(primeFactors(n))
