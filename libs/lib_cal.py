import calendar


def basic_cal(month, year):
    # then must create an object of the Calendar class
    cal = calendar.Calendar(firstweekday=-1)
    # year = 2023
    # month = 12
    year = int(year)
    month = int(month)
    print(year, month, "year month in basic cal")
    l = cal.monthdatescalendar(year, month)
    print(len(l))
    # print(l)
    return l


if __name__ == "__main__":
    l = basic_cal(12, 23)
    print(l)
