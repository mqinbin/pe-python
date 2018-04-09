from utils.my_math import PrimeHelper
import re



if __name__ == '__main__':
    primes = [x for x in PrimeHelper(1000000)]

    circular_primes = []
    for p in primes:
        pstr = str(p)
        if len(pstr)>=2 and re.match('[245680]', pstr):
            # print(p)
            continue
        cp = p
        while True:
            cp = cp % 10 * 10 ** (len(str(cp)) - 1) + cp // 10
            # print('p %d cp %d' % (p, cp))
            if cp == p:
                circular_primes.append(p)
                break
            if cp not in primes:
                break
    print(len(circular_primes))
