from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

a = x2 - x1
b = y2 - y1
z = sqrt((a*a)+(b*b))

print(f"{z:.4f}")
