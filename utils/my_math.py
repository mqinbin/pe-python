from math import sqrt, floor ,ceil

class DivisorsHelper(object):
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        # print(n)
        yield 1
        less_part = []
        for t in range(2, ceil(sqrt(self.n)) ):
            if self.n % t == 0:
                less_part.append(t)
                yield t

        sqrtn = floor(sqrt(self.n))
        if sqrtn > 1 and self.n == sqrtn * sqrtn:
            yield sqrtn

        less_part.reverse()
        for x in less_part:
            yield self.n // x