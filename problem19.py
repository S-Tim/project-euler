from datetime import date
from dateutil.relativedelta import *

current = date.fromisoformat('1901-01-01')
end_date = date.fromisoformat('2000-12-31')
one_month = relativedelta(months=1)

sundays = 0
while current <= end_date:
    if current.weekday() == 6:
        sundays += 1
    current += one_month

print(sundays)
