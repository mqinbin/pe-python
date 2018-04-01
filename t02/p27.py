from utils.my_math import PrimeHelper

if __name__ == '__main__':
    p = PrimeHelper(10000)
    primes = set()
    brange = []
    for x in p:
        if x < 1000:
            brange.append(x)
        primes.add(x)

    # n2 + an + b

    maxlen = 0
    result = None  # (a,b)
    for b in brange:
        for a in range(-b, 1000):
            len = 0
            for n in range(0, 1000):
                if (n ** 2 + a * n + b) not in primes:
                    if len > maxlen:
                        maxlen = len
                        result = (a,b)
                    break
                len += 1

    print(maxlen)
    print(result)
    print(result[0] * result[1])

    for n in range(0, 1000):
        t =(n ** 2 + result[0] * n + result[1])
        if t not in primes:
            break
        print(t ,end=' ')