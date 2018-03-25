from utils.my_math import FactorialHelper

if __name__ == '__main__':
    nums = list(range(0,10))

    factorials = [0]
    for x in FactorialHelper(10):
        factorials.append(x)

    index = 0
    lo = 0
    hi = factorials[10]
    mid = 0
    target = 1000000 - 1
    result = []
    jie = 9
    while True:

        if mid < target:
            mid += factorials[jie]
            index += 1
            continue
        elif mid > target:
            n = nums.pop(index-1)
            result.append(n)
            mid -= factorials[jie]

            index = 0
            jie -=1
            continue
        else:
            nums.reverse()
            result.extend(nums)
            break
    print("".join(map(str,result)))

    # TODO  Binary Search
    '''
        nums = list(range(0, 10))

        factorials = {}

        n = 1
        for x in FactorialHelper(10):
            factorials[n] = x
            n += 1
        print(factorials)

        index = 0
        lo_index = 0
        hi_index = len(nums)
        mid_index = len(nums) / 2
        temp = 0
        target = 1000000 - 1
        result = []
        jie = 9

        while True:
            temp = factorials[jie] * mid_index
            if temp > target:
                mid_index = (mid_index + lo_index) //2
            elif temp < target:
                mid_index = (hi_index + mid_index) //2
            





    '''