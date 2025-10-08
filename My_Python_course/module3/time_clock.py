from datetime import date, datetime

today = datetime(year=2025, day=9, month =10)
mybirthday = datetime(1982, 10, 9)
print(f'Today - {today} Birthday - {mybirthday} days total - ')
input_1 = "2025/10/09" 
# string parse time # str -> datetime
d = datetime.strptime(input_1, "%Y/%m/%d")
#delta = timedelta.days(today - mybirthday)
print(mybirthday.strftime('%d %A %B'))
#print(delta)

start_date = date(year=2022, day=24, month=2)
today_date = date(year = 2025, day = 7, month=10)

delta = today_date - start_date

print(delta)
# 
#