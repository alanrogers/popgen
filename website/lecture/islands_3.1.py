# islands_3.1.py  2 March 2023  N = 25, p0 = 1/2N 

######### DETERMINE THE GENOTYPIC FITNESSES #########
#### BY SETTING THE SELECTION PARAMETERS s AND h ####

# For the class experiment, first do the neutral case:
# s = 0, h = 0.5 (h has no effect when s = 0.)

s = 0.0
h = 0.5

# Then do all six combinations of
# s in [-0.05, 0.05], and
# h in [0, 0.5, 1] (A1 dominant, additive, A2 dominant).

####### THE GENOTYPIC FITNESSES #######

w = [1.0, 1.0 + h*s, 1.0 + s]

# IMPORT THE GRAPHICS AND RANDOM-NUMBER FUNCTIONS

from graphics import *
from random import random, randrange
from time import sleep

#### SET THE PER-GENERATION SLEEP TIME to slow things down.
#### Good choices will probably fall between 0.02 and 0.1 (seconds).

sleep_time = 0.02

# SET UP THE GRAPHICS WINDOW (note: color #1E90FF is Dodger Blue)

win = GraphWin("100 Isolated Islands", 860, 610)
win.setCoords(0, 0, 860, 610)
win.setBackground("black")

headerText = Text(Point(735,550),"Genotypic fitnesses")
headerText.setTextColor("white")
headerText.setStyle("bold")
headerText.draw(win)

selText = Text(Point(735,520),"s = %4.2f, h = %4.2f" % (s,h))
selText.setTextColor("white")
selText.setStyle("normal")
selText.draw(win)

A1A1_Text = Text(Point(685,490),"A1A1")
A1A1_Text.setTextColor("yellow")
A1A1_Text.setStyle("bold")
A1A1_W = Text(Point(685,470),"%4.2f" % (w[0]))
A1A1_W.setTextColor("yellow")
A1A1_W.setStyle("bold")

A1A2_Text = Text(Point(735,490),"A1A2")
A1A2_Text.setTextColor("light green")
A1A2_Text.setStyle("bold")
A1A2_W = Text(Point(735,470),"%5.3f" % (w[1]))
A1A2_W.setTextColor("light green")
A1A2_W.setStyle("bold")

A2A2_Text = Text(Point(785,490),"A2A2")
A2A2_Text.setTextColor("#1E90FF")
A2A2_Text.setStyle("bold")
A2A2_W = Text(Point(785,470),"%4.2f" % (w[2]))
A2A2_W.setTextColor("#1E90FF")
A2A2_W.setStyle("bold")

A1A1_Text.draw(win)
A1A1_W.draw(win)

A1A2_Text.draw(win)
A1A2_W.draw(win)

A2A2_Text.draw(win)
A2A2_W.draw(win)

sleep_Text = Text(Point(735,100),"sleep_time = %4.2f seconds" % (sleep_time))
sleep_Text.setTextColor("white")
sleep_Text.setSize(10)
sleep_Text.draw(win)

# present and next-gen grids for metapopulation
pgrid = [[0 for i in range(50)] for j in range(50)]

# members of the islands indexed by col/row
poplists = [[[] for i in range(10)] for j in range(10)]
for col in range(10):
    for row in range(10):
        for i in range(5):
            for j in range(5):
                flatcol = col*5 + i
                flatrow = row*5 + j
                poplists[col][row].append([flatcol,flatrow])

# their positions on screen
pos = [[[0,0,0,0] for i in range(50)] for j in range(50)]

for col in range(10):
    colBase = 12 + col*60
    for row in range(10):
        rowBase = 12 + row*60
        for i in range(5):
            for j in range(5):
                flatcol = col*5 + i
                flatrow = row*5 + j
                
                corner1i = colBase + i*9
                corner1j = rowBase + j*9
                corner2i = corner1i + 9
                corner2j = corner1j + 9

                pos[flatcol][flatrow][0] = colBase + i*9
                pos[flatcol][flatrow][1] = rowBase + j*9
                pos[flatcol][flatrow][2] = colBase + i*9 + 9
                pos[flatcol][flatrow][3] = rowBase + j*9 + 9


# start with p2 = 0.02
islands_p = [[0.02 for i in range(10)] for j in range(10)]
p0 = 0.02

colors = ["yellow","light green","#1E90FF"]   # #1E90FF = Dodger Blue
for i in range(50):
    for j in range(50):
        pgrid[i][j] = 0
        if j % 5 == 2 and i % 5 == 2:
            pgrid[i][j] = 1

timeText = Text(Point(735,400), "Generation %3d" % (0))
timeText.setTextColor("white")
timeText.setStyle("bold")
timeText.draw(win)

nfix = nfix1 = nfix2 = 0

fix1Text = Text(Point(735,370), "fixed A1 = %2d" % (nfix1))
fix1Text.setTextColor("white")
fix1Text.draw(win)

fix2Text = Text(Point(735,340), "fixed A2 = %2d" % (nfix2))
fix2Text.setTextColor("white")
fix2Text.draw(win)

for i in range(50):
    for j in range(50):
        ind = Rectangle(Point(pos[i][j][0],pos[i][j][1]), \
                        Point(pos[i][j][2],pos[i][j][3]))
        color = colors[pgrid[i][j]]
        ind.setOutline("black")
        ind.setFill(color)
        ind.draw(win)

win.getMouse()

gfixed = [[0 for i in range(10)] for j in range(10)]
gfixlist = []

#### START THE SIMULATION (GENERATIONS LOOP) ####

for g in range(1001):
    nfix = nfix1 = nfix2 = 0
    
    # "SLEEP" to slow the pace...
    sleep(sleep_time)
    
    for col in range(10):
        for row in range(10):
            if islands_p[col][row] == 0.0 or islands_p[col][row] == 1.0:
                nfix += 1
                if islands_p[col][row] == 0.0:
                    nfix1 += 1
                elif islands_p[col][row] == 1.0:
                    nfix2 += 1
                
                if islands_p[col][row] == 1.0 and gfixed[col][row] == 0:
                    gfixed[col][row] = g
                    gfixlist.append(g)

                continue
            
            # Reproduce by sampling from each island's fitness-biased
            # gamete pool.  First get the genotype frequencies.
            
            genums  = [0,0,0]      # this gen's genotype numbers
            genumsp = [0,0,0]      # next gen's genotype numbers
            
            for n in range(25):
                genums[pgrid[poplists[col][row][n][0]][poplists[col][row][n][1]]] += 1
            
            f = [genums[0]/25.0, genums[1]/25.0, genums[2]/25.0]
            p2 = f[2] + 0.5*f[1]
            
            wbar = f[0]*w[0] + f[1]*w[1] + f[2]*w[2]
            wbar2 = (f[2]*w[2] + 0.5*f[1]*w[1])/(f[2] + 0.5*f[1])
            p2p = p2*wbar2/wbar

            # now reproduce using p2p (selection-biased freq of A2)
            local_p2 = 0
            for n in range(25):
                offgeno = 0
                if random() < p2p:
                    offgeno += 1
                if random() < p2p:
                    offgeno += 1
                    
                # but instead of making offpop list of genotypes, just count them
                genumsp[offgeno] += 1
                local_p2 += offgeno

            islands_p[col][row] = local_p2/50.0
            
            # New minimal-replacement algorithm to speed graphical updating
            # We have genums[] and gnumsp[] for this island
            
            change = [genumsp[0] - genums[0], genumsp[1] - genums[1], genumsp[2] - genums[2]]
                
            # list genotype states to be added, and those eligible to be bumped
            add = []
            if change[0] > 0:
                for i in range(change[0]):
                    add.append(0)
            if change[1] > 0:
                for i in range(change[1]):
                    add.append(1)
            if change[2] > 0:
                for i in range(change[2]):
                    add.append(2)

            # do replacements ONLY if there is at least one addition
            if len(add) > 0:
                sub = []
                if change[0] < 0:
                    sub.append(0)
                if change[1] < 0:
                    sub.append(1)
                if change[2] < 0:
                    sub.append(2)

                # get ALL potentially eligible to drop
                candrop = []
                for i in range(5):
                    for j in range(5):
                        flatcol = col*5 + i
                        flatrow = row*5 + j
                        if pgrid[flatcol][flatrow] in sub:
                            candrop.append([flatcol,flatrow])

                # replace exactly the expected number of each declining genotype
                for newstate in add:
                    foundSpot = 0
                    while foundSpot == 0:
                        home = candrop.pop(randrange(len(candrop)))
                        gtype = pgrid[home[0]][home[1]]
                        if change[gtype] < 0:
                            pgrid[home[0]][home[1]] = newstate
                            change[gtype] += 1
                            foundSpot = 1
                            
                    ind = Rectangle(Point(pos[home[0]][home[1]][0],pos[home[0]][home[1]][1]),\
                                    Point(pos[home[0]][home[1]][2],pos[home[0]][home[1]][3]))
                    color = colors[pgrid[home[0]][home[1]]]
                    ind.setFill(color)
                    ind.draw(win)


    timeText.undraw()
    timeText = Text(Point(735,400), "Generation %3d" % (g))
    timeText.setStyle("bold")
    timeText.setTextColor("white")
    timeText.draw(win)

    fix1Text.undraw()
    fix1Text = Text(Point(735,370), "fixed A1 = %2d" % (nfix1))
    fix1Text.setTextColor("white")
    fix1Text.draw(win)

    fix2Text.undraw()
    fix2Text = Text(Point(735,340), "fixed A2 = %2d" % (nfix2))
    fix2Text.setTextColor("white")
    fix2Text.draw(win)

    if nfix == 100:
        break

# OPEN THE RESULTS FILE, APPEND A SUMMARY OF THIS RUN.

ofile = open("islands_3_results.txt","a")
ofile.write("p0 = %4.2f  s = %5.2f  h = %4.1f  fixA1 = %3d  fixA2 = %3d  g = %3d" % \
            (p0,s,h,nfix1,nfix2,g))
if len(gfixlist) > 0:
    ofile.write("  gA2fix:")
    for gen in gfixlist:
        ofile.write(" %d" % (gen))
ofile.write("\n")
ofile.close()

win.getMouse()
win.close()
