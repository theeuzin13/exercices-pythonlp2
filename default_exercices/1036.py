from math import sqrt

a, b, c = map(float, input().split())

x = ((b*b)-4*a*c)
if x < 0:
    print('Impossivel calcular')
elif a == 0:
    print('Impossivel calcular')
else:
    r1 = ((-b+sqrt(x))/(2*a))
    r2 = ((-b-sqrt(x))/(2*a))
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
