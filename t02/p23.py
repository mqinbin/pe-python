from utils.my_math import DivisorsHelper


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
    for x in range(1, 28123):
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

