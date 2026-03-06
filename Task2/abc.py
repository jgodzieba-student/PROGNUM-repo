#!/usr/bin/env python


print(f"a:")
a = float(input())

print(f"b:")
b = float(input())

print(f"c:")
c = float(input())

D = b**2 - 4*a*c

if D > 0:
    x_1 = (-b+(D)**0.5)/(2*a)
    x_2 = (-b+(D)**0.5)/(2*a)
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
elif D == 0:
    x_1 = (-b+(D)**0.5)/(2*a)
    print(f"x_2 = {x_1}")
else:
    print("There are no roots")

