def reciprocal_cycle(n):
    dividend = 1
    divider = n

    list_tuple = []
    item = None

    # dividend  / divider   = commerce  ... remainder

    while True:
        if dividend < divider:

            item = (0, dividend)
            list_tuple.append(item)
        else:
            commerce = dividend // divider
            remainder = dividend - divider * commerce
            item = (commerce, remainder)
            if item in list_tuple:
                list_tuple.append(item)
                break
            if remainder == 0:
                list_tuple.append(item)
                break

            list_tuple.append(item)
            dividend = remainder
        dividend *= 10

    # print(list_tuple)
    return list_tuple


if __name__ == '__main__':
    max = 0
    result = 0
    for n in range(2, 1000 + 1):
        l = reciprocal_cycle(n)
        start = l.index(l[-1])
        if len(l) - start > max:
            max = len(l) - start
            result = n

    print(max, result)
