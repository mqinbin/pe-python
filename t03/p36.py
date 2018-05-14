


def same_reverse(numStr: str):
    length = len(numStr)
    for i in range(length // 2):
        if numStr[i] != numStr[-1 -i]:
            return False
    return True


if __name__ == '__main__':
    # nums = []
    total = 0
    for n in range(1,1000000,2):
        if same_reverse(str(n)) and same_reverse( bin(n)[2:]):
            total += n
            # nums.append(n)
    print(total)