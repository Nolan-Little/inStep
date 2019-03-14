import datetime
import calendar
from calendar import HTMLCalendar

def month_cal(year, month, month_iter=0):
    cal = HTMLCalendar(firstweekday=6)
    cal = cal.formatmonth(theyear=year, themonth=month + month_iter, withyear=True)
    cal = cal.replace('<table ', '<table cellpadding="10" cellspacing="10" class="m-2 text-center month" border="2" ')
    return cal
