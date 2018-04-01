from math import sqrt, floor, ceil


def factorial(n):
    result = 1;
    for x in range(1, n + 1):
        result *= x
    return result


def sum_formn_tom(n, m):
    return (m - n + 1) * (m + n) // 2


def prime_factors(n):
    ps = PrimeHelper(n)
    result = []

    for p in ps:
        times = 0
        while n >= p:
            if n % p == 0:
                times +=1
                n /= p
            else:
                break
        if times:
            result.append((p,times))
        if n < p:
            break
    return result


known_prime_nums = [2, 3, 5, 7]


class PrimeHelper(object):
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        global known_prime_nums

        for n in known_prime_nums:
            if n <= self.max:
                yield n
            else:
                return

        i = known_prime_nums[-1] + 1
        while i <= self.max:
            sq = ceil(sqrt(i))
            for p in known_prime_nums:
                if i % p == 0:
                    break
                if p > sq:
                    known_prime_nums.append(i)
                    yield i
                    break
            i += 1


class FibonacciHelper(object):

    def __iter__(self):
        prev = 1
        current = 1
        next = 0
        yield prev
        yield current
        while True:
            next = prev + current
            yield next
            prev = current
            current = next


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
