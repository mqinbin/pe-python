from utils.decorations import cache_method


@cache_method
def count_groups(total: int, li_coins: tuple) -> int:
    if len(li_coins) == 0 or total == 0:
        return 0

    result = 0
    for c in range(total // li_coins[0], -1, -1):
        # print(c, li_coins, result)
        takes = li_coins[0] * c
        resume = total - takes
        if takes > total:
            break
        elif takes < total:
            result += count_groups(resume, li_coins[1:])
        else:
            result += 1
    return result


if __name__ == '__main__':
    print(count_groups(200, (200, 100, 50, 20, 10, 5, 2, 1)))
    # print(cache)
