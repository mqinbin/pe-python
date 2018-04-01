import fractions
if __name__ == '__main__':
    result = []
    for a in range(10, 99):
        if a % 10 == 0:
            continue
        aa = str(a)
        for x in range(1, 9):
            other = [(10 * x + int(aa[1])), (10 * int(aa[1]) + x)]
            for o in other:
                if o <= a:
                    continue
                if a * x == int(aa[0]) * o:
                    print('%d / %d' % (a, o))
                    result.append(fractions.Fraction(a,o))

        for x in range(1, 9):
            other = [(10 * x + int(aa[0])), (10 * int(aa[0]) + x)]
            for o in other:
                if o <= a:
                    continue
                if a * x == int(aa[1]) * o:
                    print('%d / %d' % (a, o))
                    result.append(fractions.Fraction(a, o))

    f = fractions.Fraction(1,1)
    mutply = 1
    for f in result:

        mutply *= f.denominator
        mutply /= f.numerator

    print(int(mutply))