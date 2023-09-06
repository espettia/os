"""Simple MMS (memory management system) simulation.

Some general notes:

"Page" means always "virtual page number".  We do not track physical
page numbers in this class, because we do not need to.

When performing "read" operations, we do not really read anything.  We
just pretend to do so.  Read the method documentation for details on
what is really done.

We do not provide a write() function here.  Thus, "to swap out" means
removing a page from memory, not necessarily writing it to disk."""


# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.


class MMS:
    
    """Memory management system (generic).

    Includes page replacement algorithm, output function and simple
    statistics.

    Derived classes implement the actual page replacement
    algorithm."""
    

    def __init__(self, num):
        
        """Set memory size to num pages.  Initialize."""
        
        # pages is initialized as an empty list which will store page
        # numbers later.
        
        self.pages = []

        self.memsize = num

        # Track swap-ins.

        self.swapins = 0

        # Track swap-outs.  Even if, in this class, swapping out
        # doesn't mean that anything has been written to disk, this
        # information might be useful in some situations.
        
        self.swapouts = 0

        # Maybe derived classes will need a random number generator,
        # so we create it here.  We use a constant seed, in order to
        # get reproducible results.  If you do not like this,
        # overwrite self.rand after instantiation.

        import random
        self.rand = random.Random(42)


    def read(self, page):
        
        """Read a page.

        Do nothing else than generating a pagefault() if the requested
        page is not in memory.

        Derived classes might implement some algorithm-specific
        code."""

        if not page in self.pages:
            self.pagefault(page)


    def create(self, page):

        """Create a page.

        Append the page number to the end of pages.

        This method should not be invoked directly, as it does not
        check if there is enough space in memory.  Use read()
        instead."""

        self.pages.append(page)


    def pagefault(self, page):
        
        """Create a new page in memory.

        If memory is full, remove a page from memory before."""

        # Usually len(self.pages) is not greater than self.memsize.
        # However, it may occur that memsize has been reduced.  In
        # this case we must remove pages until the number of pages
        # falls below memsize.

        while len(self.pages) >= self.memsize:
            self.swapout()
            self.swapouts += 1

        # Now create the page.  We do not do this here directly
        # because derived classes might need to provide their own
        # create() methods.

        self.create(page)
        self.swapins += 1


    # Derived classes must define swapout(self), which is the page
    # replacement algorithm.  swapout(self) removes a page from the
    # pages variable and returns the number of the removed page.
    

    def output(self):

        """Output page numbers to stdout, sorted by the order in which they will be removed.

        This is rather brute force, but for memory sizes that fit onto
        screen it should not be a problem.  However, derived classes
        might implement more efficient (i.e. algorithm specific)
        output functions."""

        import copy

        # Copy this MMS and remove all pages, tracking the order.

        mmscopy = copy.deepcopy(self)
        numlist = []
        while mmscopy.pages:
            numlist.append(mmscopy.swapout())

        numlist.reverse()

        # Output the page which will be removed next as first entry.
        
        print " ".join(map(lambda x: str(x), numlist))
