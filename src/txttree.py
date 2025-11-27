##include <stdio.h>
##include <assert.h>
##include <string.h>
##include <math.h>
##include <poco/err.h>
##include "gtreec.h"
#
#typedef struct BranchDat BranchDat;
#
#struct TxtTreePlot {
#    double lca;      /* time of last common ancestor */
#    int    nLeaves;  /* number of leaves */
#    int    hdim;     /* horizontal dimension of m */
#    double hmax;     /* max plottable horizontal value */
#    int    vdim;     /* vertical dimension of m */
#    int    rootlen;  /* spaces devoted to root */
#    double hscale;   /* hunits per unit of time */
#    double vscale;   /* vunits per leaf */
#    char  *m;        /* matrix of character values */
#};
#
#struct BranchDat {
#    EventType type;
#    double length;
#    int nmut;
#    TreeNode *left, *right;
#};
#
#static int  ndx(TxtTreePlot *ttp, int i, int j);
#static void TxtTreePlot_dump(const TxtTreePlot *ttp, FILE *fp);
#static void BranchDat_init(BranchDat *bd, const TreeNode *node,
#						const MutInterface *mif);
#

class BranchDat:
    # Initialize BranchDat with data from current branch.
    #
    # Node is a list with three entries:
    #
    #  node[0] is length of branch to parent
    #  node[1] is left child (another node)
    #  node[2] is right child
    def __init__(self, node):
        EventType t;

        if node == None:
            self.length = 0.0
            self.left = None
            self.right = None
        else:
            self.length = node[0]
            self.left = node[1]
            self.right = node[2]
        return

class TxtTreePlot:

    def dump(self):
        print "TxtTreePlot data dump:"
        print "   lca    =%g" % self.lca
        print "   nLeaves=%d" % self.nLeaves
        print "   hdim   =%d" % self.hdim
        print "   hmax   =%g" % self.hmax
        print "   vdim   =%d" % self.vdim
        print "   rootlen=%d" % self.rootlen
        print "   hscale =%g" % self.hscale
        print "   vscale =%g" % self.vscale


    def __init(self, lca, nLeaves, hunits):
        if lca == 0.0:
            print "TxtTreePlot.__init__: empty tree"
            lca = 1.0
        self.lca = lca
        self.nLeaves = nLeaves
        self.hdim = hunits
        self.vscale = 2.0
        self.vdim = nLeaves * self.vscale
        self.rootlen = 4
        self.hscale = (hunits - self.rootlen) / float(lca)
        self.hmax = (self.hdim - 1.0) / self.hscale;

        # m is a matrix of characters on which to draw.
        # Initially, each row is blank.
        # Each row ends with '\n'
        row = self.hdim*' '
        row += '\n'
        self.m = ''
        for i in range(0, self.vdim):
            self.m += row

    def ndx(self, i, j):
        return i*self.hdim + j
    
    def print(self):
        print self.m

    def __str__(self):
        return self.m

    def plot(self, root):

        vpos = mid = 0.0;
        hpos = self.draw(root, vpos, mid)
        self.putRule(hpos, mid, self.hmax, mid)

    # Recursive algorithm for drawing a tree.
    #
    # On entry:
    #  node points to current node of tree
    #  *vpos should equal 0.0.
    #  *mid's value doesn't matter.
    #
    # On return:
    #  *node is unchanged
    #  *vpos  equals the number of leaves in the tree.
    #  *mid is the vertical coordinate of the middle of the segment separating
    #     the two top-level clades.
    # The function returns the horizontal coordinate of the tree's root.
    draw(self, node, vpos, mid):
        double top, bottom, hpos;

        if node == None:
            mid = vpos;
            return 0

        # set BranchDat structure
        bd = BranchDat(node) 
    
        hpos = self.draw(bd.left, vpos, mid)
        top = mid
        hpos = self.draw(bd.right, vpos, mid, mif)
        bottom = mid

        if hpos > 0 && top != bottom:
            self.putRule(hpos, bottom, hpos, top)

        if top == bottom:
            mid = top
        else:
            mid = bottom + 0.5 * (top - bottom)
        if bd.length == HUGE_VAL:
            bd.length = 0.0
        if bd.length > 0.0:
            buff = 20*' '
            print "%d" % bd.nmut
            len = len(buff)  # won't work
            h = hpos + bd.length/2.0;
            self.rescale(h, mid, i, j)
            j -= len/2
            if j < 0:
                j = 0
	
            self.putRule(hpos, mid, hpos + bd.length, mid)
            if bd.nmut > 0:
                for k in range(0,len):
                    self.m[self.ndx(i,j+k)] = buff[k];

        if hpos == 0.0:
            vpos += 1.0
        return hpos + bd.length


void
TxtTreePlot_rescale(TxtTreePlot *ttp, double x, double y,
		    int *i, int * j) {
#if 1
    *i = 0.5 + ttp->vscale * y;
#else
    *i = y;
#endif
    *j = 0.5 + ttp->hscale * x;

    if(*i < 0 || *i >= ttp->vdim || *j < 0 || *j >= ttp->hdim) {
	fflush(stdout);
	fprintf(stderr,"Error in TxtTreePlot_rescale @%s:%d\n",
		__FILE__,__LINE__);
	fprintf(stderr,"*i=%d; should be in [0, %d]\n",
		*i, ttp->vdim-1);
	fprintf(stderr,"*j=%d; should be in [0, %d]\n",
		*j, ttp->hdim-1);
	fprintf(stderr,"(x,y) = (%g,%g)\n", x, y);
	TxtTreePlot_dump(ttp, stderr);
	exit(1);
    }
}

void
TxtTreePlot_putRule(TxtTreePlot *ttp, double x1, double y1,
		    double x2, double y2) {
    int i1, i2, j1, j2, k;

    TxtTreePlot_rescale(ttp, x1, y1, &i1, &j1);
    TxtTreePlot_rescale(ttp, x2, y2, &i2, &j2);

    if(i1 != i2 && j1 != j2)
	poco_eprintf("slanted lines are illegal @%s:%d",
		     __FILE__,__LINE__);

    if(i1 > i2) {
	k = i1;
	i1 = i2;
	i2 = k;
    }
    if(j1 > j2) {
	k = j1;
	j1 = j2;
	j2 = k;
    }

    if(j1 == j2) {  /* vertical line */
	for(k = i1; k <= i2; ++k)
	    ttp->m[ndx(ttp, k, j1)] = '|';
    }else if(i1 == i2) { /* horizontal line */
	for(k = j1; k <= j2; ++k) {
	    int l = ndx(ttp, i1, k);
	    if(ttp->m[l] == ' ')  /* don't overwrite verticals */
		ttp->m[l] = '-';
	}
    }
}

