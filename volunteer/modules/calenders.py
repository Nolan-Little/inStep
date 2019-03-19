import datetime
import calendar
from calendar import HTMLCalendar

def month_cal(year, month, month_iter=0):
    '''generates a month formatted calender from python standard calender lib based on provided month, year

    Arguments:
        year {date object} -- python datetime.datetime.now().year
        month {date object} -- python datetime.datetime.now().month

    Keyword Arguments:
        month_iter {int} -- iterater for creating months in the future from datetime.now() (default: {0})

    Returns:
        htmlstring -- html string calendar formatted by month
    '''

    now = datetime.datetime.now()
    cal = HTMLCalendar(firstweekday=6)
    cal = cal.formatmonth(theyear=year, themonth=month + month_iter, withyear=True)
    cal = cal.replace('<table ', '<table data-month={} data-year={} cellpadding="10" cellspacing="10" class="m-2 text-center month" border="2" '.format(month + month_iter, year))
    if month_iter != 0 or year != now.year:
        cal = cal.replace('<table ', '<table hidden data-month={} data-year={} cellpadding="10" cellspacing="10" class="m-2 text-center month" border="2" '.format(month + month_iter, year))

    return cal
