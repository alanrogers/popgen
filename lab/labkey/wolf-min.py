#!/usr/bin/env python3
from random import random

w = [3246, 3449, 2897, 2841, 3635, 3932]  # counts from Wolf's white die
r = [3407, 3631, 3176, 2916, 3448, 3422]  # counts from Wolf's red die

min_w = min(w)
min_r = min(r)
tail_w = 0.0   # count number of simulated minima <= than min_w
tail_r = 0.0   # count number of simulated minima <= than min_r

print("min_w:", min_w)
print("min_r:", min_r)

nreps = 1000

for rep in range(nreps):
    count = [0,0,0,0,0,0]           # count[i] is number of times we roll i+1

    for roll in range(20000): # 20000 rolls of a fair die
        spots = int(6*random())     # uniform on [0,1,2,3,4,5]
        count[spots] += 1

    m = min(count)
    if m <= min_w:
        tail_w += 1
    if m <= min_r:
        tail_r += 1

print("A fraction %f of simulated minima is as small as min_w." % \
    (tail_w/float(nreps)))
print("A fraction %f of simulated minima is as small as min_r." % \
    (tail_r/float(nreps)))
    
    
