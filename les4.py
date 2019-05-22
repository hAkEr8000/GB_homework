from random import random

A1 = int(input())
A2 = int(input())
a = int(random() * (A2 - A1 + 1)) + A1
print(a)

A1 = float(input())
A2 = float(input())
a = random() * (A2 - A1) + A1
print(round(a, 3))

A1 = ord(input())
A2 = ord(input())
a = int(random() * (A2 - A1 + 1)) + A1
print(chr(a))
