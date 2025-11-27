from pgen import bnldev

def mnldev(n, p):
    """
    Return a deviate from a Multinomial random variable.
    On entry, n should be a positive integer and p a vector
    of values that are proportional to probabilities.
    """
    yvec = []
    i = 0
    while i < len(p)-1:
        y = bnldev(n, p[i]/float(sum(p[i:])))
        y = int(y)
        n -= y
        yvec.append( y )
        i += 1
    yvec.append(n)
    return yvec


def test_mnldev():
    for i in range(10):
        x = mnldev(10000000000000, [0.1, 0.3, 0.1])
        print(x)

if __name__ == '__main__':
    test_mnldev()
