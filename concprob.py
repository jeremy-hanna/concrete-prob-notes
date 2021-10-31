# concprob

# *** CLASSICAL ***
from fractions import Fraction

def P(event, space, favorable=set.intersection, cases=len):
    "The probability of an event in a given sample space"
    if callable(event):
        event = { x for x in space if event(x) }
    n, d = (cases(favorable(event, space)), cases(space))
    if isinstance(space, Dist):
        # use floating point division for distribution probabilities
        return n / d
    else:
        return Fraction(n, d)

import itertools
def combos(items, n):
    "All combinations of n items as a space-separated str"
    return set(map(' '.join, itertools.combinations(items, n)))

def balls(color, n):
    "Generate a set of n balls of a color"
    return { color + str(i) for i in range(1, n+1) }

def select(color, n, space):
    "Select n balls of a given color from a sample space"
    return { s for s in space if s.count(color) == n }

def choose(n, c):
    "Number of ways to choose c items from a list of n length"
    from math import factorial
    return factorial(n) // (factorial(n - c) * factorial(c))


# *** Distributions ***
from collections import Counter
class Dist(Counter):
    "A Distribution of {outcome: frequency} pairs"
    def cases(outcomes):
        return sum(outcomes.values())
    def favorable(event, space):
        if callable(event):
            event = { x for x in space if event(x) }
        return Dist({x: space[x]
                    for x in space if x in event})

def DistP(event, space):
    ""
    return P(event, space, Dist.favorable, Dist.cases)


def joint(A, B, combine='{}{}'.format):
    """The joint distribution of two independent distributions.
    Result is all entries of the form {'ab': frequency(a) * frequency(b)}"""
    return Dist({combine(a, b): A[a] * B[b]
                 for a in A for b in B})
