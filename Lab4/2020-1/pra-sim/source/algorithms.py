"""Several page replacement algorithms.

The most important methods in this module are the swapout methods.
They remove a page from memory and return its number."""


# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.


import mms
import inspect
import sys

class FIFO(mms.MMS):

    """FIFO (first-in-first-out) algorithm."""

    def swapout(self):

        num = self.pages[0]
        del self.pages[0]
        return num

    # That's all.  Pretty simple, uh?


class SecondChance(mms.MMS):

    """Second Chance algorithm."""

    def __init__(self, num):

        """Create R bit dictionary."""

        mms.MMS.__init__(self, num)

        # self.r is a dictionary mapping page numbers to R bits.

        self.r = {}


    def swapout(self):

        # Do not delete any page with R bit set.  While first page has
        # R bit set, unset R bit and move page to the end of the list.

        while self.r[self.pages[0]]:
            self.r[self.pages[0]] = 0
            self.pages.append(self.pages[0])
            del self.pages[0]

        # Now we can be sure that the first page's R bit is not set.

        # Store number of first page for later returning

        num = self.pages[0]

        # Remove entry from R bit dictionary and remove page number
        # from pages list.
        
        del self.r[num]
        del self.pages[0]

        return num


    def read(self, page):

        """Set R bit."""

        mms.MMS.read(self, page)

        self.r[page] = 1


    def create(self, page):

        """Create page and initialize entry in R bit dictionary."""

        mms.MMS.create(self, page)

        self.r[page] = 0
        

class LRU(mms.MMS):

    """LRU (least recently used) algorithm."""

    def swapout(self):

        num = self.pages[0]
        del self.pages[0]
        return num


    def read(self, page):

        """Move page to the end of the list."""

        # Call read() method of base class.

        mms.MMS.read(self, page)

        # We need remove(), because page is a value, not an index.

        self.pages.remove(page)
        self.pages.append(page)


class Aging(mms.MMS):

    """Aging algorithm."""

    def __init__(self, num, bits=32, shift=16):

        """Initialize aging dictionary, bit set width and shifting
        frequency."""

        mms.MMS.__init__(self, num)

        self.configure(bits, shift)

        # aging maps page numbers to aging bit sets

        self.aging = {}

        # self.instr counts read instructions.  Every self.shift
        # instructions, the aging bits are shifted.
        
        self.instr = 0L


    def configure(self, bits, shift):

        """Set bit set width and shifting frequency.

        Initialize self.firstbit as number with first bit set.  It
        will be right-shifted every self.shift instructions."""

        if bits > 0:
            self.firstbit = 1L << (bits - 1)
        else:
            self.firstbit = 0

        self.shift = shift



    def swapout(self):

        # Create list (minlist) of indices with smallest aging value.
        # Start with index 0.
        
        minlist = [0]
        
        for i in range(1, len(self.pages)):

            # self.aging[self.pages[minlist[n]]] is equal for all n, so we can use
            # element zero.
            
            if self.aging[self.pages[i]] == self.aging[self.pages[minlist[0]]]:
                minlist.append(i)
            elif self.aging[self.pages[i]] < self.aging[self.pages[minlist[0]]]:
                minlist = [i]
                
        index = self.rand.choice(minlist)
        num = self.pages[index]
        del self.aging[num]
        del self.pages[index]
        return num


    def read(self, page):

        """Set first bit of page."""

        mms.MMS.read(self, page)

        self.aging[page] |= self.firstbit

        # Increment instruction counter and shift if necessary.

        self.instr += 1
        if not self.instr % self.shift:
            for i in self.aging.keys():
                self.aging[i] >>= 1


    def create(self, page):

        """Initialize aging counter for page."""

        mms.MMS.create(self, page)

        self.aging[page] = 0L


class NRU(Aging):

    """NRU (not recently used) algorithm."""

    def read(self, page):

        """Set bit of page."""

        mms.MMS.read(self, page)

        # Aging uses "|= self.firstbit" here. That's the main
        # difference.

        self.aging[page] = 1

        # Increment instruction counter and shift if necessary.

        self.instr += 1
        if not self.instr % self.shift:
            for i in self.aging.keys():
                self.aging[i] = 0


class Optimal(mms.MMS):

    """Optimal algorithm."""

    def __init__(self, num, alist=None):

        """Initialize instruction counter, access list and nextaccess dict.

        alist is the list of pages to read."""

        mms.MMS.__init__(self, num)

        self.alist = alist

        # nextaccess maps page numbers to time (i.e. instruction
        # number) of next access.

        self.nextaccess = {}

        self.instr = 0
        

    def read(self, page):

        """Increment instruction counter."""

        mms.MMS.read(self, page)

        self.instr += 1

        # Look into future and store next access time in nextaccess.

        self.nextaccess[page] = -1

        for i in range(self.instr, len(self.alist)):
            if page == self.alist[i]:
                self.nextaccess[page] = i
                break


    def swapout(self):

        """Remove page which will not be read for the longest time."""

        index = 0

        for i in range(len(self.pages)):
            if self.nextaccess[self.pages[i]] == -1:
                index = i
                break
            elif self.nextaccess[self.pages[i]] > self.nextaccess[self.pages[index]]:
                index = i

        num = self.pages[index]
        del self.nextaccess[num]
        del self.pages[index]
        return num


# Put all classes which do not start with an underscore character into
# index.

index = []
vars()
i = None   # Avoid "RuntimeError: dictionary changed size during iteration"
for i in vars().keys():
    if inspect.isclass(vars()[i]) and issubclass(vars()[i], mms.MMS) and not vars()[i].__name__.startswith('_'):
        index.append(i)
index.sort()

i2 = []
for i in index:
    i2.append(vars()[i])

index = i2

