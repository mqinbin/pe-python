from utils.my_math import FibonacciHelper

if __name__ == '__main__':
    target = 10 ** (1000 -1)
    count = 0
    for num  in  FibonacciHelper():
        count +=1
        if num > target:
            break
    print(count)
