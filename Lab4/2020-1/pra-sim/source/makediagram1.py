#!/usr/bin/python

"""Make a diagram."""

# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.

import algorithms
import access
import random
import simulate
import Gnuplot


d = []    # List of gnuplot data
for i in [algorithms.FIFO, algorithms.SecondChance, algorithms.NRU,
          algorithms.LRU, algorithms.Aging]:
    # List of tupels of (ws_length, page_faults_to_accesses_ratio).
    ratios = []
    for j in range(1, 61):
        mms = i(64)    # Instantiate.
        mms.shift = 200
        mms.firstbit = 1 << 7
        ws = access.wsmake(mem=range(10000), rand=random, size=j)
        mms.alist = access.makealist(range(10000), ws, random, 0.95, 100000)
        ratios.append((j, simulate.simulate(mms, mms.alist)))
        print i.__name__ + ": " + str(j)
    d.append(Gnuplot.Data(ratios, title=i.__name__, inline=1))

g = Gnuplot.Gnuplot()
g('set style data lines')
g('set yrange [0:]')
g('set terminal epslatex monochrome')
g('set output "diagram1.eps"')
g('set xlabel "working set size in pages"')
g('set ylabel "ratio of page faults to accesses"')
g.plot(*d)

print "\nNow move diagram1.* to ../"
