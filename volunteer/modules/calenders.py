import datetime
import calendar
from calendar import HTMLCalendar

def month_cal(year, month, month_iter=0):
    now = datetime.datetime.now()
    cal = HTMLCalendar(firstweekday=6)
    cal = cal.formatmonth(theyear=year, themonth=month + month_iter, withyear=True)
    cal = cal.replace('<table ', '<table cellpadding="10" cellspacing="10" class="m-2 text-center month" border="2" ')
    if month_iter != 0 or year != now.year:
        cal = cal.replace('<table ', '<table hidden cellpadding="10" cellspacing="10" class="m-2 text-center month" border="2" ')

    return cal
