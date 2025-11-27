import bisect

class Tabulator:
    """
    Tabulate numerical data into bins.

    Alan Rogers 2007
    """
    def __init__(self, low=0.0, high=1.0, nBins=5):
        """
        Tabulator(...) -> new Tabulator

        low and high specify the range of the data to be tabulated.

        nBins specifies number of bins
        """
        self.infinity = 1e30000  # Python lacks support for inf
        self.low = float(low)
        self.high = float(high)
        self.binsize = (self.high - self.low)/nBins
        self.nBins = nBins+2     # for values outside range
        self.counts = self.nBins*[0]

        # lbound = [-inf, ..., high] size = nBins
        # ubound = [low, ..., inf] size=nBins
        self.ubound = [self.low + i*self.binsize \
                       for i in range(0, self.nBins)]
        self.ubound[self.nBins-2] = self.high
        self.ubound[self.nBins-1] = self.infinity

    def bin(self, x):
        """
        return index of bin containing x
    
        bin 0           : values < low
        bins 1..nBins-2 : values in [low,high]
        bin nBins-1     : values > high
        """
        i = bisect.bisect_left(self.ubound, x)
        assert i >= 0
        assert i < self.nBins
        return i

    def __iadd__(self, x):
        '"self += x" increments count in bin containing x'

        i = self.bin(x)
        self.counts[i] += 1
        return self

    def __getitem__(self, i):
        'self[i] returns the number of items in bin i'
        assert i >= 0
        assert i < self.nBins
        return self.counts[i]

    def upperBound(self, i):
        "Upper bound of i'th bin"
        return self.ubound[i]

    def lowerBound(self, i):
        "Lower bound of i'th bin"
        assert i >= 0
        assert i < self.nBins
        if i == 0:
            return -self.infinity
        return self.ubound[i-1]

    def sampleSize(self):
        'Sample size'
        return sum(self.counts)

    def __str__(self):
        'Convert to string'
        s = "%-24s %s\n" % ("Range", "Count")
        for i in range(0, self.nBins):
            s += "[%9.5f ...%9.5f] %5d\n" % (self.lowerBound(i),
                                          self.upperBound(i),
                                          self.counts[i])
        s += "%-24s %5d" % ("Total", self.sampleSize())
        return s

    def clear(self):
        'Set all counts to zero'
        self.counts = self.nBins*[0]
    
def test():
    'Test class Tabulator'

    tab = Tabulator(1.0, 2.0, 4)
    assert tab[tab.bin(1.1)] == 0
    tab += 1.1
    assert tab[tab.bin(1.1)] == 1
    tab += 1.1
    assert tab[tab.bin(1.1)] == 2
    tab += 1.222
    assert tab[tab.bin(1.1)] == 3
    tab += 1.3
    assert tab[tab.bin(1.1)] == 3
    assert tab[tab.bin(1.3)] == 1
    assert tab[tab.bin(1.8)] == 0
    assert tab.sampleSize() == 4
    print(tab)

    tab.clear()
    assert tab.sampleSize() == 0
    assert tab[tab.bin(1.3)] == 0

if __name__ == '__main__':
    test()

