from random import random

twoN = 40
num_A1 = 8
num_A2 = twoN - num_A1
p = float(num_A1)/float(num_A1 + num_A2)

print("\ngen %3d  [%3d A1 %3d A2]  p = %5.3f" %(gen, num_A1, num_A2, p))

while p > 0.0 and p < 1.0:
    gen += 1
    num_A1 = num_A2 = 0
    for trial in range(twoN):
        if random() < p:
            num_A1 += 1
        else:
            num_A2 += 1

    p = float(num_A1)/float(num_A1 + num_A2)
    print("gen %3d [%3d A1 %3d A2] p = %5.3f" %(gen, num_A1, num_A2, p))
