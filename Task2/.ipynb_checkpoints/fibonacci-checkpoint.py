#!/usr/bin/env python


s = 1
f = 1
i = 0
while i<98:
    f+=s
    s=f-s
    i+=1

print(f)