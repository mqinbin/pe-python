from utils.my_math import PrimeHelper
import re

if __name__ == '__main__':
    target = []
    len_num_map = {}
    for p in PrimeHelper(1000000):
        pstr = str(p)
        if re.match('[024568]', pstr):
            continue
        length = len(pstr)
        if length not in len_num_map:
            len_num_map[length] = {}
        len_num_map[length][p] = 1
        yes = True
        lp = pstr
        rp = pstr

        for t in range(length-1):
            lp = lp[1:]
            rp = rp[:-1]
            if int(lp) in len_num_map[len(lp)] and int(rp) in len_num_map[len(rp)]:
                continue
            else :
                yes = False
                break

        if yes:
            target.append(p)

    # print(len_num_map)
    print(target)