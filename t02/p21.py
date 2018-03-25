from utils.my_math import DivisorsHelper


if __name__ == '__main__':
    # print(sum( helper(220)))
    # print(sum( helper(284)))


    is_list = []
    not_list = []
    for t in range(2, 10000 + 1):
        if t in is_list or t in not_list:
            continue
        else:
            o = sum( DivisorsHelper(t))
            if o == t or o > 10000:
                continue
            if t == sum(DivisorsHelper(o)):
                is_list.append(t)
                is_list.append(o)
            else:
                not_list.append(t)

    print(is_list)
    print(sum(is_list))
