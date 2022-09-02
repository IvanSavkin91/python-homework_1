# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from difflib import Match
import math


print ('Введите координату A1')
a1 = int (input ())
print ('Введите координату B1')
b1 = int (input ())
print ('Введите координату A2')
a2 = int (input ())
print ('Введите координату B2')
b2 = int (input ())
c = math.sqrt((a2-a1)**2 + (b2-b1)**2)
print(round(c, 3))