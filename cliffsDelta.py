from __future__ import division


def cliffsDelta(lst1, lst2,
                dull = [0.147,  # small
                        0.33,  # medium
                        0.474  # large
                        ][0]):
    """Returns true if there are more than 'dull' differences"""
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    return abs(d) > dull


def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two


def _cliffsDelta():
    """demo function"""
    lst1 = [1,2,3,4,5,6,7]
    for r in [1.01, 1.1, 1.21, 1.5, 2]:
        lst2 = map(lambda x: x*r, lst1)
        print(r, cliffsDelta(lst1, lst2))  # should return False
