#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

print("Choose R for rock, P for paper, S for scissors:")
rps = input()
RPS = np.random.randint(1,3+1) #each nr will have an assosiated R = 1, P = 2, or S = 3

if rps == "R":
    if RPS == 1:
        print("Draw! Both chose rock!")
    elif RPS == 2:
        print("You loose! The computer chose paper!")
    else:
        print("You won! The computer chose scissors!")
elif rps == "P":
    if RPS == 2:
        print("Draw! Both chose paper!")
    elif RPS == 3:
        print("You loose! The computer chose scissors!")
    else:
        print("You won! The computer chose rock!")
elif rps == "S":
    if RPS == 3:
        print("Draw! Both chose scissors!")
    elif RPS == 1:
        print("You loose! The computer chose rock!")
    else:
        print("You won! The computer chose paper!")
else:
    print("not valid")
    pass
    

