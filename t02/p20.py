from functools import *
def jie(n):
    result =1
    i = 1
    while i <n:
        result *= i
        i+=1
    return result
if __name__ == '__main__':
    s = str(jie(100))
    # print()
    print(sum(map(int, [x for x in s])))