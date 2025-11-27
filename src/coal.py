nGenes = 3   # number of genes in sample
theta = 1    # 2 X (population size) * (mutation rate)

from random import random, randint, expovariate
import math

# A function to print branch lengths.
def printTree(node, indent):
    if node == None:
        return
    print("%s %8.4f" % ("+"*indent, node[0])) # print curr branch length
    printTree(node[1], indent+1)             # print left subtree
    printTree(node[2], indent+1)             # print right subtree
    return

# Construct a list of length nGenes.  Each entry represents a
# gene in the sample.  Each entry is itself a list containing
# three entries: (0) the length of branch to parent, (1) pointer
# to left child, (2) pointer to right child.  In this initial list,
# the branch length to parent is 0 and the child pointers are None.
nodevec = [ [0.0, None, None] for i in range(0, nGenes)]

# Each pass through loop joins two nodes.  At end, there is
# only one node left: the root of the gene tree.
while len(nodevec) > 1:
    nNodes = len(nodevec)
    h = nNodes*(nNodes-1)/(2*theta)   # hazard of a coalescent event
    t = expovariate(h)                # time until next coalescent event
    for node in nodevec:              # add this time to each node.
        node[0] += t
    i = randint(0,nNodes-1)           # choose 2 nodes to join
    j = randint(0,nNodes-2)
    if j >= i:
        j += 1
    nodevec[i] = [0.0, nodevec[i], nodevec[j]] # join them
    if j < nNodes-1:                     
        nodevec[j] = nodevec[nNodes-1]
    del nodevec[nNodes-1]             # reduce length of nodevec

assert len(nodevec) == 1              # check for error
    
print("Branch Lengths in Coalescent Tree:")
printTree(nodevec[0], 0)
