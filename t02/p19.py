def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


mods = {1: 3, 3: 3, 5: 3, 7: 3, 8: 3, 10: 3, 12: 3,
        4: 2, 6: 2, 11: 2, 9: 2, }


def mod_seven(year, month):
    if month != 2:
        return mods[month]
    elif is_leap_year(year):
        return 1
    else:
        return 0


def get_week_by_year(year):
    result = 0
    if year > 1900:
        for y in range(1900, year + 1):
            result += 365
            result += is_leap_year(y)
        return result % 7
    elif year < 1900:
        for y in range(1900, year, -1):
            result -= 366
            result -= is_leap_year(y)
            return (result % 7 + 7) % 7
    else:
        return 1


def get_times(start_day=(1900, 1), end_day=(2000, 1), week=1):
    '''
    :param start_day: (year,month) all begin with 1, include
    :param end_day:    (year,month) all begin with 1, exclude
    :param week:  sunday is 0 ;monday as 1
    :return: the week times
    '''
    week_dict = {}
    day_one_week = get_week_by_year(start_day[0])
    print('year %d  day_one_week %d ' %(start_day[0] ,day_one_week))
    for year in range(start_day[0], end_day[0] + 1):
        for month in range(1, 13):

            if year >= end_day[0] and month >= end_day[1]:
                # 返回结果
                return week_dict[week]
            else:
                print('year %d, month %d, week %d' % (year, month, day_one_week))
                if year == start_day[0] and month < start_day[1]:
                    continue
                else:
                    increase(week_dict, day_one_week)
                day_one_week = (day_one_week + mod_seven(year, month)) % 7



def increase(d, key):
    if key in d:
        d[key] = d[key] + 1
    else:
        d[key] = 1


if __name__ == '__main__':
    print(get_times((1901, 1), (2001, 1), 0))

# days = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
#         4: 30, 6: 30, 11: 30, 9: 30, }
#
#
# def days(year, month):
#     if month == 2:
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#             return 29
#         else:
#             return 28
#     else:
#         global days
#         return days[month]
