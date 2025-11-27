from math import log10, floor, ceil

class axis:
    def __init__(self, v, output_size, nticks=5):
        self.low = min(v)
        self.high = max(v)
        self.outsize = int(output_size)

        # Get tick values, the number of character positions needed to
        # print them, and the format to be use.
        self.tickval, self.lblwid, self.tickfmt = \
                      lblaxis(self.low,self.high,nticks)

        # Reset high and low if necessary to accomodate ticks
        if self.tickval[-1] > self.high:
            self.high = self.tickval[-1]
        if self.tickval[0] < self.low:
            self.low = self.tickval[0]

        # Set scale parameter
        if self.high == self.low:
            self.scale = 1.0
        else:
            self.scale = (self.outsize-1.0)/(self.high-self.low)

        # Get the indices of the tick values
        self.tickndx = []
        for tval in self.tickval:
            self.tickndx.append(self.ndx(tval))


    # Return index of val
    def ndx(self, val):
        assert val >= self.low
        assert val <= self.high
        i = int(round(self.scale*(val - self.low)))
        assert i >= 0
        assert i < self.outsize
        return i

maxxcess = 0.6
roundval = [1.0, 1.5, 2.0, 2.5, 5.0]

def lblaxis(asklow, askhigh, askntic):
    """
    Generate labels for an axis.  Input parameters:

    asklow : desired low value of axis
    askhigh: desired high value
    askntic: number of tick marks desired

    Function returns (tic, lng, fmt), where

    tic is a list of floats, the values at which tick marks should be
        placed, and
    lng is the number of character positions needed for printing
        tick labels.
    fmt is a string that specifies the format to be used in printing
        tick labels.

    For example, the tick marks can be printed like this:

      for value in tic:
          print fmt % value

    The range of tick mark values and the number of tick marks should
    be close to the values requested, but will probably not be identical.
    The function tries to generate a list of values that will be pretty.
    """

    high = askhigh
    low = asklow
    assert high > low, "lblaxis: low > high"
    n = askntic

    for i in range(5):
	oldhigh = high
	oldlow = low
	w = (high - low) / (n - 1.0)
	x = log10(w)
	exp10 = floor(x)
	y = 10.0**(x - exp10)
	y = 0.5 * floor(2.0 * y + 0.5)
	# y should now be close to one of the values in roundval
	i0 = 0
        for i in range(1, len(roundval)):
            if abs(y - roundval[i]) < abs(y - roundval[i0]):
		i0 = i

	# width of interval is roundval[i0] * 10^exp10
	w = roundval[i0] * pow(10.0, exp10)

	# calculate new low
	low = ceil(oldlow / float(w)) * w
        if low - asklow > maxxcess * w:
	    low = w*(ceil(oldlow / float(w)) - 1.0) # new low

	# calculate new high
	high = w*floor(oldhigh / float(w))
        if askhigh - high > maxxcess * w:
	    high = w*(floor(oldhigh / float(w)) + 1.0)
        if oldhigh == high or oldlow == low:
            break

    askntic = n = int((high - low) / float(w) + 1.5) # rounds to nearest int

    # fill tick-mark vector
    tic = []
    for i in range(n):
	tic.append(low + i * w)

    eps = (high - low)*0.05

    # calculate printing format
    lng0, frac, fmt0 = prwid(low, eps)
    lng1, frac, fmt1 = prwid(high, eps)
    if lng1 > lng0:
        return (tic, lng1, fmt1)
    return (tic, lng0, fmt0)


def prwid(w, precision):

    # Step 1: round w to a value determined by the precision
    # needed.
    s = "%f" % w
    s = s.strip('0')
    for frac in range(0,len(s)):
        r = round(w, frac)
        if abs(r-w) <= precision:
            w = r
            break
    fmt = "%%1.%df" % frac
    s = fmt % w
    if '.' in s:
        s = s.rstrip('0')
        s = s.rstrip('.')

    # lng is length of whole string
    lng = len(s)
    if lng == 0:
        lng = 1

    # format string
    fmt = "%%%d.%df" % (lng, frac)
    return (lng, frac, fmt)

# Plots on terminals w/o graphics capabilities.
# On entry: 
#       x is a float vector of x-axis values
#       y is a float vector of y-axis values
# Function writes plot on standard output
def charplot(x, y, nticks=5, output_height=24, output_width=78):

    yax = axis(y, output_height)
    left_pad = yax.lblwid+1
    output_width -= left_pad
    xax = axis(x, output_width)

    blank_row = (output_width)*[' ']
    chrmat = [blank_row[:] for i in range(output_height)]


    # create plot matrix
    for i in range(1, output_height):     # draw side lines
        chrmat[i][0] = '|'
        chrmat[i][output_width - 1] = '|'
    for i in range(output_width):         # draw top & bottom lines
        chrmat[0][i] = '-'
        chrmat[output_height-1][i] = '-'

    for ndx in xax.tickndx:     # tics on x axis 
        chrmat[0][ndx] = '+'
        chrmat[output_height-1][ndx] = '+'

    for ndx in yax.tickndx:     # tics on y axis
        chrmat[ndx][0] = '+'
        chrmat[ndx][output_width-1] = '+'

    for xval, yval in zip(x,y):     # data points 
        chrmat[yax.ndx(yval)][xax.ndx(xval)] = '*'

    # create list of y axis labels
    ylab = []
    for i in range(yax.outsize):
        ylab.append(yax.lblwid*' ')
    for ndx, val in zip(yax.tickndx, yax.tickval):
        ylab[ndx] = yax.tickfmt % val

    assert(yax.outsize == len(chrmat))

    # print chrmat
    for i in range(len(chrmat)):
        ndx = len(chrmat) - i - 1
        row = chrmat[ndx]
        line = ''.join(row)
        print("%s %s" % (ylab[ndx], line))
    s = ''
    curr_pos = -left_pad
    for ndx, val in zip(xax.tickndx, xax.tickval):
        lbl = xax.tickfmt % val
        lbl = lbl.strip()
        if '.' in lbl:
            lbl.rstrip('0')
            lbl.rstrip('.')
        wid = len(lbl)
        halfwid = wid/2
        skip = ndx - halfwid - curr_pos
        s += skip*' '
        s += lbl
        curr_pos += skip + wid
    print(s)

def test_charplot():
    xv = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    yv = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    charplot(xv, yv, 5, 18, 50)

test_charplot()
