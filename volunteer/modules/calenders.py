import datetime
import calendar
from calendar import HTMLCalendar

def month_cal():
    now = datetime.datetime.now()
    cal = HTMLCalendar(firstweekday=6)
    cal = cal.formatmonth(theyear=now.year, themonth=now.month, withyear=True)
    cal = cal.replace('<table ', '<table cellpadding="5" cellspacing="5" class="m-2 text-center month" border="2" ')
    return cal
