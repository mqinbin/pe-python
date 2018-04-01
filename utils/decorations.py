cache: dict = {}  # total -> ( (coins)-> count)


def cache_method(func, *args):
    def result(*args):
        global cache
        key = tuple(args)
        if key in cache:
            return cache[key]
        else:
            value = func(*args)
            cache[key] = value
            return value

    return result
