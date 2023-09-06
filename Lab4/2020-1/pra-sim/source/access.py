"""Memory access simulation.

All ws* methods modify the working set in place and only change one
element.  For continuous working set modification, call them
repeatedly.

The following assumptions are being made throughout the entire module:

mem is a sequence containing page numbers, representing the memory.

ws is a sequence containing page numbers, representing the working
set.  All elements of ws are contained in mem.

rand is a random number generator, e.g. the module random or an
instance of random.Random."""


# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.


def access(mem, ws, rand, probab):

    """Return page number to access.

    probab is the probability with which a page from working set is
    chosen."""

    if rand.random() < probab:
        return rand.choice(ws)
    else:
        while 1:
            p = rand.choice(mem)
            if not p in ws:
                return p


def makealist(mem, ws, rand, probab, length):

    """Return access list.

    probab is the probability with which a page from working set is
    chosen, length is the list's length."""

    if not ws or not mem:
        return []

    # alist stores tupels of (page, taken_from_ws).

    alist = []

    # Create alist with pages from ws.

    for i in range(length):
        alist.append((rand.choice(ws), 1))

    # Replace (1 - probab) of all elements with a random element from mem.

    for i in range(int(length * (1 - probab) + 0.5)):
        while 1:
            index = rand.randint(0, length - 1)

            # If page has not yet been replaced.
            
            if alist[index][1]:
                while 1:
                    x = rand.choice(mem)
                    if not x in ws:
                        alist[index] = (x, 0)
                        index = None
                        break
                    
            if index is None:
                break

    # Transform (page, taken_from_ws) into page

    for i in range(length):
        alist[i] = alist[i][0]

    return alist
        


def wsmake(mem, rand, size):

    """Return a working set of size pages all contained in mem."""

    ws = []

    for i in range(size):
        while 1:
            num = rand.choice(mem)
            if not num in ws:
                break
        ws.append(num)

    return ws


def wsmove(mem, ws, rand):

    """Move working set."""

    # Choose a page number which is not contained in ws.

    while 1:
        num = rand.choice(mem)
        if not num in ws:
            break

    # Delete random element of ws.

    del ws[rand.randrange(len(ws))]

    ws.append(num)


def wsextend(mem, ws, rand):

    """Extend working set."""

    # Choose a page number which is not contained in ws.

    while 1:
        num = rand.choice(mem)
        if not num in ws:
            break

    ws.append(num)


def wsshrink(ws, rand):

    """Shrink working set."""

    del ws[rand.randrange(len(ws))]
