from math import sqrt, floor, ceil


def factorial(n):
    result = 1;
    for x in range(1, n + 1):
        result *= x
    return result


def sum_formn_tom(n, m):
    return (m - n + 1) * (m + n) // 2


class FactorialHelper(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        result = 1;
        x = 1
        while x <= self.n:
            result *= x
            yield result
            x += 1


class DivisorsHelper(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # print(n)
        yield 1
        less_part = []
        for t in range(2, ceil(sqrt(self.n))):
            if self.n % t == 0:
                less_part.append(t)
                yield t

        sqrtn = floor(sqrt(self.n))
        if sqrtn > 1 and self.n == sqrtn * sqrtn:
            yield sqrtn

        less_part.reverse()
        for x in less_part:
            yield self.n // x
