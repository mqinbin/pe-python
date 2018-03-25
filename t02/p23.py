from utils.my_math import DivisorsHelper,sum_formn_tom


# 28123

def just_num(n):
    factors = sum(DivisorsHelper(n))
    return factors - n;
    # if factors < n:
    #     return  -1
    # elif factors> n:
    #     return 1
    # else:
    #     return 0


if __name__ == '__main__':


    deficients = []
    perfects = []
    abundants = []
    for x in range(1, 28124):
        t =  just_num(x)
        if t < 0 :
            deficients.append(x)
        elif t>0:
            abundants.append(x)
        else:
            perfects.append(x)

    print( 'deficients')
    print( deficients)
    print( 'perfects')
    print( perfects)
    print( 'abundants')
    print( abundants)

    s = set()
    for m in abundants:
        for n in abundants:
            sum = m + n
            if sum>28123:
                break
            s.add(sum)

    total = sum_formn_tom(1,28123)
    for m in s:
        total -= m

    print(total)