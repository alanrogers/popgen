# Calculate the means, variances, and covariance of two data vectors.
# Skips observations in which either data vector has a missing value.
# Returns mx, vx, my, vy, covxy
def bivariate_moments(xdata, ydata):
    mx = my = vx = vy = cov = 0.0
    n = 0
    for x, y in zip(xdata, ydata):
        if x==None or y==None:
            continue
        n += 1
        mx += x
        my += y
        vx += x*x
        vy += y*y
        cov += x*y
    n = len(xdata)
    assert n == len(ydata)
    mx /= float(n)
    my /= float(n)
    vx /= float(n)
    vy /= float(n)
    cov /= float(n)

    cov -= mx * my
    vx -= mx * mx
    vy -= my * my
    return mx, vx, my, vy, cov
