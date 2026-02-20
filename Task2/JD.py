#!/usr/bin/env python

print(f"Enter Year:")
Y = float(input())

print(f"Enter Month:")
M = float(input())

print(f"Enter Day:")
D = float(input())

JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5

print(JD)