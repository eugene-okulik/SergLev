from _datetime import datetime

simple_date = "Jan 15, 2023 - 12:05:33"

phyton_date = datetime.strptime(simple_date, "%b %d, %Y - %H:%M:%S")

print(datetime.strftime(phyton_date, "%B"))
print(datetime.strftime(phyton_date, "%d.%m.%Y, %H:%M"))
