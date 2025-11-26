3. wolf.py

4. driftmut.py

5. coal_S.py

6. coin_ci.py

7. drseln.py

8. This lab is meant to be done interactively, at the Python command
prompt. Here is my interaction:

    >>> from pgen import *
    >>> hds = hapmap_dataset(hapmap_fname(22, "JPT"))
    hapmap_dataset:Skipped 45481 SNPs w/ missing or monomorphic data; kept 11235
    >>> snp = hds[83]
    >>> snp.alleles
    ['C', 'T']
	>>> # 1. Allele 0 is C.
    >>> snp.gtype.count(0)
    29
	>>> # 2. There are 29 copies of allele 0 in the data.
    >>> p = snp.mean/2.0
	>>> p
    0.2
	>>> # 3. The relative frequency of allele 0 is 0.2.
    >>> 2*p*(1-p)
    0.32000000000000006
	>>> # 4. The expected (Hardy-Weinberg) heterozygosity is 0.32
    >>> snp.gtype.count(1)/float(snp.sampleSize)
    0.3111111111111111
	>>> # 5. The observed heterozygosity is 0.31
    >>> snp.position
    15638201
	>>> #6. The SNP is at nucleotide position 15638201 on the chromosome.
	
9. haphet.py

10. twoloc.py

11. hapspec.py

12. rscan.py

13. lactase.py
