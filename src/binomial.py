# binomial.py

from random import random
from math import exp, log, tan, sqrt, floor, pi

nold = (-1)
pold = (-1.0)
pc = plog = pclog = en = oldg = 0.0
cof = (76.18009172947146,  -86.50532032941677,  24.01409824083091, \
       -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5)

def gammln(xx):
	"""
	Return natural log of Gamma function.
	"""

	y = x = xx
	tmp = x + 5.5
	tmp -= (x+0.5)*log(tmp)
	ser = 1.000000000190015
	for j in range(6):
		y += 1
		ser += cof[j]/y
	return -tmp + log(2.5066282746310005*ser/x)


def bnldev(n, pp):
	"""
	Return a random deviate drawn from the Binomial distribution
	with parameters n (a positive integer) and pp (a probability).
	"""

	global nold, pold, pc, plog, pclog, en, oldg

	if pp <= 0.5:
		p = pp
	else:
		p = 1.0 - pp

	am = n*p

	if n < 25:
		bnl = 0.0
		for j in range(1, n+1):
			if random() < p:
				bnl += 1.0

	elif am < 1.0:
		g = exp(-am)
		t = 1.0
		for j in range(n):
			t *= random()
			if t < g:
				break
		bnl = j

	else:
		if n != nold:
			en = n
			oldg = gammln(en + 1.0)
			nold = n;

		if p != pold:
			pc = 1.0 - p
			plog = log(p)
			pclog = log(pc)
			pold = p

		sq = sqrt(1.0*am*pc)

		while 1 == 1:
			while 1 == 1:
				angle = pi*random();
				y = tan(angle)
				em = sq*y + am
				if em >= 0 and em < (en+1.0):
					break
			em = floor(em)
			t = 1.2*sq*(1.0+y*y)*exp(oldg-gammln(em+1.0) \
				- gammln(en-em+1.0) + em*plog + (en-em)*pclog)
			if random() < t:
				break
		bnl = em

	if p != pp:
		bnl = n - bnl

	return bnl


# TRY IT OUT!
def test():
	pp = 0.5
	n = 10
	s1 = s2 = s0 = 0.0

	for i in range(10000):
		x = bnldev(n,pp)
		s1 += x
		s2 += x*x
		s0 += 1

	mean = s1/s0
	sd = sqrt((s2 - s1*mean)/(s0-1.0))
	print(mean,sd,int(s0))


if __name__ == '__main__':
    test()
