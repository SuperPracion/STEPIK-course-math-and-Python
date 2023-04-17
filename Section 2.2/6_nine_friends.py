from math import sqrt

side_a = int(input())

s6 = (3 * sqrt(3) / 2) * side_a ** 2
sqa = 3 * pow(side_a, 2)
stria = 6 * ((side_a / 2) ** 2 * sqrt(3)) / 4

print(round(s6 + sqa + stria))
