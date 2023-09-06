#!/usr/bin/python

"""Make a diagram."""

# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.

import algorithms
import access
import simulate

import Gnuplot

import random


shiftrange = range(1, 20)
ws = access.wsmake(mem=range(10000), rand=random, size=5)

alist = []
for i in range(500000):
    alist.append(access.access(range(10000), ws, random, 0.95))
    if not i % 10:
        access.wsmove(range(10000), ws, random)
    if not i % 1000:
        print "alist: " + str(i)
        
ratios = []
for i in shiftrange:
    mms = algorithms.Aging(6, bits=4, shift=i)    # Instantiate.
    ratios.append((i, simulate.simulate(mms, alist)))
    print "Shifting frequency: " + str(i)

g = Gnuplot.Gnuplot()
g('set style data points')
g('set yrange[0:]')
g('set terminal epslatex monochrome')
g('set output "diagram2.eps"')
g('set xlabel "shifting frequency in read-instructions per shift"')
g('set ylabel "ratio of page faults to accesses"')
g.plot(Gnuplot.Data(ratios, inline=1))

print "\nNow move diagram2.* to ../"
