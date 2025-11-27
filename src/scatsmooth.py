def scatsmooth(x,y,n):
    """
    Smooth a set of (x,y) data by dividing the range of
    x values into n equally-spaced bins, and calculating
    the average y-value within each bin.

    Function returns (x_mid, y_mean)
    where x_mid is a vector of n midpoints of bins,
    and y_mean is the vector of means within the bins.
    """
    lo_x = min(x)
    hi_x = max(x)

    assert hi_x > lo_x
    scale = (n-1.0)/(hi_x-lo_x)

    ym = n*[0.0]  # vector of means
    yn = n*[0]    # vector of sample sizes
    step = (hi_x-lo_x)/float(n)

    for xval, yval in zip(x,y):
        ndx = int(round(scale*(xval-lo_x)))
        ym[ndx] += yval
        yn[ndx] += 1

    x_midpoint = []
    for ndx in range(n):
        if yn[ndx] > 0:
            ym[ndx] /= float(yn[ndx])
        x_midpoint.append(lo_x + (ndx+0.5)*step)

    return (x_midpoint, ym)

# Smooth data using an exponentially weighted moving average.  x is
# the data vector to be smoothed, and b is a parameter that controls
# the amount of smoothing.  Choose a value that satisfies 0 <= b < 1.
# If b=0, no smoothing is done.  Larger values of b produce more
# smoothing.
def expmovav(x, b=0.85):
    n = len(x)
    y0 = [(1.0-b)*x[0]]
    for i in range(1, n):
        val = (1.0-b)*x[i] + b*y0[i-1]
        y0.append( val  )

    y1 = n*[None]
    y1[n-1] = (1.0-b)*x[n-1]
    for i in range(n-2, -1, -1):
        val = (1.0-b)*x[i] + b*y1[i+1]
        y1[i] = val
    y = []
    for yy0, yy1 in zip(y0, y1):
        y.append(0.5*(yy0 + yy1))
    return y

def test_expmovav():
    from random import random
    n = 5
    x = [i-0.5*n for i in range(n)]
    y = [i-0.5*n + random() for i in range(n)]
    #x = [i for i in range(n)]
    #y = [1 for i in range(n)]

    ys = expmovav(y, 0.0)
    print("Results of expmovav:")
    for xval, yval in zip(x, ys):
        print(xval, yval)

def test_scatsmooth():
    from random import random
    n = 5
    x = [i-0.5*n for i in range(n)]
    y = [i-0.5*n + random() for i in range(n)]

    xs, ys = scatsmooth(x,y, 10)
    print("Results of scatsmooth:")
    for xval, yval in zip(xs, ys):
        print(xval, yval)

#test_scatsmooth()
test_expmovav()

    
    
    

    
