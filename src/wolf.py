#!/usr/bin/python

# Calculate chi-squared goodness of fit on list x
def chisq(x):
    # expected: all counts are equal
    e = sum(x)/float(len(x))
    s = 0.0
    for y in x:
        s += (y-e)**2 / e
    return s

# Counts on faces 1-6 on Wolf's red and white dice
red = [3407, 3631, 3176, 2916, 3448, 3422]
white = [3246, 3449, 2897, 2841, 3635, 3932]

print("red chisq =", chisq(red), "white chisq =", chisq(white))
print("df =", len(red)-1)
