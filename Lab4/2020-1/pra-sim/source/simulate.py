"""Do the real simulation."""

# Written by Felix Wiemann <http://www.ososo.de/>, licensed under GPL-2.

def simulate(mms, alist, skip=0):

    """Apply accesses in alist on mms.

    Return ratio of page faults to accesses, leaving the first skip
    accesses out of consideration."""

    for i in range(len(alist)):
        if i == skip:
            mms.swapouts = 0
        mms.read(alist[i])

    return float(mms.swapouts) / (len(alist) - skip)
