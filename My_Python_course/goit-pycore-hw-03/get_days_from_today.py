# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між
#  заданою датою і поточною датою.
from datetime import datetime, date

#date = input("Input the date, format 'YYYY-MM-DD'': ")
inp_date = "2021-09-18"

def get_days_from_today(date: str) -> int: 
    try:
        inpt_date = datetime.strptime(inp_date,"%Y-%m-%d")       # converting from string to datetime
    except ValueError:
        return 'Input format doesnt match. Try again: "YYYY-MM-DD"'
    today = datetime.now()                                   # todays current date 
    diff = today - inpt_date                                 # days from user date to current date
    int_diff = int(diff.days)                                # converting from timedeltaobject to int
    return int_diff

print(f"{get_days_from_today(date)}")