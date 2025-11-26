# Return the variance of the values in xvec
def var(xvec):
    m = msq = 0.0
    for x in xvec:
        m += x
        msq += x*x
    n = float(len(xvec))
    m /= n                 # mean
    msq /= n               # mean square
    return msq - m*m       # variance

x = [5, 25, 36, 37, 41, 50, 60, 73, 75, 99]
y = [15, 16, 21, 44, 49, 62, 71, 73, 78, 94]

print("Var(x):", var(x))
print("Var(y):", var(y))
