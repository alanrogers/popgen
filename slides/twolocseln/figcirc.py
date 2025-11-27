#\!/usr/bin/python
import math

degToRad = 2.0*math.pi/360.0

def polToRect(theta, r, xc=0.0, yc=0.0):
    theta *= degToRad
    return (xc + r*math.cos(theta), yc + r*math.sin(theta))

def mkPie(theta, r=1.0, xc=0.0, yc=0.0):
    print "\\circulararc 360 degrees from %f %f center at %f %f" % \
          (xc + r, yc, xc, yc)
    arcl = 270 - 0.5*theta
    arcr = 270 + 0.5*theta
    xl, yl = polToRect(arcl, r, xc, yc)
    print "\\plot %f %f %f %f /" % (xc, yc, xl, yl)
    xr, yr = polToRect(arcr, r, xc, yc)
    print "\\plot %f %f %f %f /" % (xc, yc, xr, yr)

    print "\\setshadesymbol <z,z,z,z> ({.})"
    print "\\setshadegrid span <3.5pt> point at %f %f" % (xc, yc)

    step = 20
    nsteps = 1+int(math.floor(0.5*theta/step))
    if nsteps < 3:
        nsteps = 3
    step = 0.5*theta/float(nsteps)
    slope = (yc - yl)/(xc - xl)
    print "\\vshade"
    # left half of shaded region
    for i in range(nsteps+1):
        phi = arcl + i*step
        x, y0 = polToRect(phi, r, xc, yc)
        y1 = yl + slope*(x - xl)
        print "%f %f %f" % (x, y0, y1)

    # right half of shaded region
    for i in range(1, nsteps+1):
        phi = 270 + i*step
        x, y0 = polToRect(phi, r, xc, yc)
        y1 = yc - slope*(x - xc)
        print "%f %f %f" % (x, y0, y1)
    print "/"
        
    return

mkPie(90, 1, 1, 1)
mkPie(60, 0.8, 3, 1)    
