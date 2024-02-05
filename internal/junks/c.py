import calendar


def basic_cal(year, month):
    # then must create an object of the Calendar class
    cal = calendar.Calendar(firstweekday=-1)
    year = 2023
    month = 12
    l = cal.monthdatescalendar(year, month)
    logging.info(len(l))
    logging.info(l)
    return l
