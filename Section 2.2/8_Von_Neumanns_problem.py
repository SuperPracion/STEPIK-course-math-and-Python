from sys import stdin

l, v1, v2, um = [int(num) for num in stdin]

print(int(l / (v1 + v2) * um))