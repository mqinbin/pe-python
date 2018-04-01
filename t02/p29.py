from utils.my_math import PrimeHelper, prime_factors


def to_simple_tuple(n, pow):
    pass


def pow_tuple(input, pow):
    '''
    :param input:  ( (prime_factor ,  pow) ,....)
    :return:
    '''
    return tuple([(x[0], x[1] * pow) for x in input])


if __name__ == '__main__':
    print(pow_tuple(prime_factors(15),3))

    # s = set()
    #
    # for a in range (2, 100 +1):
    #     for b in range(2, 100 + 1):
    #         s.add(a**b)
    #         s.add(b**a)
    #
    # print(len(s))
