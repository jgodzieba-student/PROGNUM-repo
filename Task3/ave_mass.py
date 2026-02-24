#!/usr/bin/env python

masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e+22]
mass2 = []
for m in masses:
    if m <= 7.349e+22:
        mass2.append(m)
m1 = set(masses)
m2 = set(mass2)
new = m1 - m2
print(new)

sm = masses[6:]
print(sm)

average = sum(sm)/len(sm)
print(average)