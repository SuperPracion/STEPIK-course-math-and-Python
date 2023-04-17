from math import *

a_side = int(input())
b_side = int(input())
c_side = int(input())
p = (a_side + b_side + c_side) / 2

print(a_side + b_side + c_side)
print(sqrt(p * (p - a_side) * (p - b_side) * (p - c_side)))