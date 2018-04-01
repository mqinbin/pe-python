# 5*5:
# 5**2 * 4 - (5-1)* 6
# 4n**2 - 6n + 6


def sum_of_spiral_diagonals(n):
    result = 1
    for n in range(3, n+1, 2):
        result += 4 * n ** 2 - 6 * n + 6
    return result



if __name__ == '__main__':
    print(sum_of_spiral_diagonals(1001))