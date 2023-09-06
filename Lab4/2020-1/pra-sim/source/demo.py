#!/usr/bin/python -i

"""Demo script."""

# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.

import string
import re

def e_text(s):

    """Print and execute s."""

    if s == "":
        return

    print ">>> " + s.splitlines()[0]
    for i in s.splitlines()[1:]:
        print "... " + i
        
    exec s in globals()


def i_text(s):

    """Interpret s.

    The syntax is as follows:

    Normal text, which is directly dumped to stdout.

    ---
    python(command):
       with{output}.dumped[to].stdout
    ---
    
    *** Press return to continue.

    If no string is supplied after "*** ", use default."""

    s = s.lstrip()

    s = re.sub(re.compile(r"^\>\>\> .*$(\n[>.]{3} .*$)*", re.MULTILINE), lambda x: "---\n" +
               re.sub(re.compile("^....", re.MULTILINE), "", x.group(0)) + "\n---", s)

    execstring = None

    for i in s.splitlines():

        # If an execution block is started or stopped.

        if i == "---":

            # Start.
            
            if execstring is None:
                execstring = ""

            # Stop.
            
            else:
                e_text(execstring)
                execstring = None

        # If we wait for return and aren't inside an execution block.
                
        elif i.find("***", 0, 3) != -1 and execstring is None:
            if i.find("*** ", 0, 4) != -1:
                i = i[4:]
            else:
                i = "Press return to continue"
            raw_input("\n-------------------- " + i + " --------------------\n")

        else:

            # Are we inside an execution block?
            
            if execstring is not None:

                if i.strip() == "":
                    continue

                # Space at the beginning?

                elif re.match("^\s", i):
                    execstring += i + "\n"

                # If there is no space, execute the last execstring.
                
                else:
                    e_text(execstring)
                    execstring = i + "\n"
                    
            else:
                print i
    

i_text(r"""
Hi!

I am a demo script script and I will show you how to use the
page-replacement-algorithms-simulation-script-collection.  I presume
that you already know the basics, this script is only about the
simulation.

Sometimes, I will execute Python commands.  I will print them behind
the usual Python prompt (">>> " and "... ") before executing and you will see
their output (if any).  If you see any error messages, something went
wrong and you should stop me by pressing Ctrl+C and solve the problem.

>>> print "This is an example."

Don't panic when you see the output appearing faster than you can read
it, I will wait for you with this message:

***

Here we go ...

First of all, we import the module which contains the page replacement
algorithm classes.

>>> import algorithms

algorithms.index contains a list of all defined classes.

>>> print algorithms.index

This doesn't look too nice, but we can also obtain the classes' names:

***

>>> for i in algorithms.index:
...     print i.__name__

So these are the algorithms currently implemented.

All algorithm classes are memory management systems utilizing a
certain algorithm and are derived from the base class 'MMS' defined in
module 'mms' (both of which we do not directly use).

***

Now, we want to test one of them.  At first, let's use the simplest
one, the FIFO algorithm.

>>> fifo = algorithms.FIFO(5)

fifo is now a memory management system (which uses the FIFO algorithm
for swapping out pages) consisting of 5 physical pages.  The number of
virtual pages is unlimited, the MMS (memory management system) doesn't
care of this.  Let's read some pages.

***

---
fifo.read(4)
fifo.read(34)
fifo.read(18)
fifo.read(11)
---

Internally, the pages have not been 'read' but the MMS has ensured
that they are in memory.  As the MMS doesn't track pages which are
swapped out (i.e. on hard disk), there is no difference between
swapping in a page from hard disk and newly creating a page.  Keep
this in mind, we will come back to it later.

The memory now contains the following pages:

>>> fifo.output()

***

The MMS tracks the number of swap-ins and swap-outs:

>>> print fifo.swapouts

That's obvious, nothing has been swapped out, as the memory still
isn't full.

>>> print fifo.swapins

Here you see that the MMS 'thought' that the newly created pages had
to be swapped in from hard disk.

***

---
fifo.read(15)
fifo.output()
fifo.read(8)
fifo.output()
print fifo.swapins
print fifo.swapouts
---

Here we can see that page 4, which is the oldest page, has been
swapped out, i.e. removed from memory.

***

When reading a page which is already contained in memory, it won't be
swapped in a second time, of course:

---
fifo.output()
fifo.read(11)
fifo.output()
print fifo.swapins
print fifo.swapouts
---

Nothing has changed.

***

Let's start implementing the simulation of a program's memory access
behavior.

Most programs do not access their allocated memory evenly
distributedly.  Instead, they have a certain set of very frequently
accessed pages which is called the 'working set'.

The working set is an extremely important concept for the design of
memory management systems (and user space programs): If there is no
working set, all implementable page replacement algorithms will
perform approximately equally well (or rather 'badly', not 'well'),
because what they do is trying to remove a page which probably won't
be accessed for a long time, which is impossible if all pages'
probabilities to be accessed are equal.

***

Thus, a program's memory access behavior can be roughly defined using
only three parameters:

- The total allocated memory.
- The working set.
- The probability that at any instruction the program will access a
  page contained in the working set (usually at something like 99%).

***

First of all, we create a memory consisting of 20 pages.

>>> mem = range(20)
>>> print mem

It's simply a list containing (virtual) page numbers.

Let's create a working set of four pages.

>>> ws = range(4)
>>> print ws

***

In order to create a list of pages to access, we use the function
makealist(mem, ws, rand, probab, length).  mem and ws are
self-explanatory, rand is a random number generator (e.g. the module
'random' or an instance of random.Random), probab is the probability
with which a page from working set is accessed and length is the
access-list's length.

>>> import access
>>> import random
>>> alist = access.makealist(mem, ws, random, 0.9, 10)
>>> print alist

As you can see, exactly nine elements (i.e. 90%) of 'alist' are
contained in 'ws'.

***

This was just a demonstration.  For the access list to be useful, it
must be much larger.  We use 10000 elements:

>>> alist = access.makealist(mem, ws, random, 0.9, 10000)

We need a new, empty FIFO:

>>> fifo = algorithms.FIFO(6)

Six physical pages for a working set of four pages should be OK.

***

Now we read the pages in alist.

>>> for i in alist:
...     fifo.read(i)
>>> print fifo.swapins
>>> print fifo.swapouts

""")

i_text(r"""
At """ + str(int(float(fifo.swapins) / 100 + 0.5)) +
 r"""% of all accesses the accessed page had to be swapped in from
harddisk.

***

Let's try LRU.

---
lru = algorithms.LRU(6)
for i in alist:
    lru.read(i)
print lru.swapins
print lru.swapouts
---

Much better.

***

In order to automate the simulation, there is a function simulate(mms,
alist, skip=0) in module 'simulate'.

>>> import simulate
>>> print simulate.simulate.__doc__

As long as we use alists generated by access.makealist, there is not
much point in setting skip.

***

>>> for i in algorithms.index:
...     # Instantiate.
...     mms = i(6)
...     # Store alist in mms.alist, as this is needed by algorithms.Optimal
...     mms.alist = alist
...     # Do the simulation and print the result, "14%" instead of "0.137777"
...     print i.__name__ + ": " + str(int(simulate.simulate(mms=mms,
...             alist=alist) * 100 + 0.5)) + "%"

***

Some algorithms must or may be configured.

E.g. the Optimal algorithm needs to know the alist in order to be able
to look into the future.  This can be achieved by supplying it as
second parameter of the constructor or by setting the instance's
attribute 'alist', as we did above.

***

The Aging algorithm needs to know two things: The bit field's width
and the shifting frequency.  They can be configured by supplying them
as second and third parameter of the constructor or by calling
configure(bits, shift):

>>> print algorithms.Aging.configure.__doc__

Of course, you can also set the instance's attributes 'firstbit' and
'shift'.  Read configure()'s source on how to do this.

Often, however, you won't need to care of all this, as the constructor
provides reasonable defaults.

***

Let's draw some diagrams.

We need gnuplot-py for that.  gnuplot-py needs gnuplot, of course, and
the Numerical Python Extension.  If one of the next commands fails,
you should keep in mind the error messages, abort this script with
Ctrl+C and ensure everything is correctly installed.

>>> import Gnuplot

***

We want to visualize how the algorithms behave at different working
set sizes.  The calculation will take a few seconds.

---
d = []    # List of gnuplot data
for i in algorithms.index:
    # List of tupels of (ws_length, page_faults_to_accesses_ratio).
    ratios = []
    for j in range(1, 11):   # Iterate from 1 to 10.
        mms = i(10)    # Instantiate.
        ws = access.wsmake(mem=range(10000), rand=random, size=j)
        mms.alist = access.makealist(range(10000), ws, random, 0.95, 3000)
        ratios.append((j, simulate.simulate(mms, mms.alist)))
    d.append(Gnuplot.Data(ratios, title=i.__name__))
---

*** Press return to plot the diagram

---
g = Gnuplot.Gnuplot()
g('set style data lines')
g('set yrange [0:]')
g.plot(*d)
---

***

Of course the diagram was completely useless, because it was far from
accurate and we do not know what exactly we were simulating, but, hey,
it looked cool, didn't it?

Now we get even cooler.  We plot a three-dimensional diagram.  Wow.

We simulate an Aging algorithm, with the following axis configuration:

x: working set size
y: bit field length
z: page-fault-to-access ratio

***

Please wait ...

---
# List of lists of page-fault-to-access-ratios.
ratios = []
for i in range(1, 11):   # Iterate bit field length from 1 to 10.
    ratios.append([])
    for j in range(1, 11):    # Iterate working set length from 1 to 10
        mms = algorithms.Aging(11, bits=i, shift=10)    # Instantiate.
        ws = access.wsmake(mem=range(10000), rand=random, size=j)
        alist = access.makealist(range(10000), ws, random, 0.95, 5000)
        ratios[i - 1].append(simulate.simulate(mms, alist))
---

*** Press return to plot the diagram

---
g = Gnuplot.Gnuplot()
g('set style data lines')
g('set hidden3d')
g('set ticslevel 0')
g('set zrange [0:]')
g.splot(Gnuplot.GridData(ratios, range(1, 11), range(1, 11),binary=0))
---

***

I hope I have been able to provide you with the knowledge of the basic
concepts used in this simulation package.  In order to run your own
simulations, you will probably have to read the doc-strings and the
source.

After this script terminates, the Python session will persist so that
you are directly able to play around with the existing environment.
Issue EOF (i.e. Ctrl+D) to exit.

Have fun!

***

""")
