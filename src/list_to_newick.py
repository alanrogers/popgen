# Convert tree from internal format into phylip format.  Internal format
# represents each node as a list:
#
#    [left_child, right_child, branch_length_to_parent]
#
# For terminal (leaf) nodes, left_child and right_child equal None.
# For internal nodes, they are lists in the same format.  For the
# root, branch_length_to_parent equals 0.  All other nodes have
# positive branch lengths. A complete tree with 3 leaves might look
# like:
#
#    [[None,None,1.2], [[None,None,0.2],[None,None,0.2], 1.0], 0]
#
# Phylip format is similar, except that leaves are not lists.  They
# are strings of form "species name":branch_length_to_parent.
# The tree above becomes
#
#    (A:1.2, (B:0.2,C:0.2):1.0)
#
# Arguments:
#
#   node: a list in internal format, as described above.  Ordinarily,
#         the function will be handed the root node.
#
#   ctr: a list containing one entry, which represents the number
#        of nodes that have been previously been printed.  If the
#        calling function sets ctr=[0], then leaves will be numbered
#        1,2,3,...  If this is the behavior you want, then simply omit
#        this argument in the calling function. 
#
# Returned value: a string in Phylip format.
def list_to_phylip(node, ctr=[0]):
    s = ""
    if node[0] == None: # We're at a leaf
        assert node[1] == None # Sanity check
        ctr[0] += 1
        s += "leaf"
        s += str(ctr[0])
        s += ":%f" % node[2]
    else:               # We're at an internal node
        s += "("
        s += list_to_phylip(node[0], ctr)
        s += ","
        s += list_to_phylip(node[1], ctr)
        s += ")"
        if node[2] > 0:
            s += ":%f" % node[2]
    return s


tree = [[None,None,1.2], [[None,None,0.2],[None,None,0.2], 1.0],0]
print(tree)
print(list_to_phylip(tree))
