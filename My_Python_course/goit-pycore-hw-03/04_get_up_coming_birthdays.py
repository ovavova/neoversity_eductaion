""" У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день
народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить
інформацію про ім'я користувача та його день народження. Оскільки дні народження
колег можуть припадати на вихідні, ваша функція також повинна враховувати це та
переносити дату привітання на наступний робочий день, якщо необхідно.   """  
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.10.09"},
    {"name": "Jane Smith", "birthday": "1990.10.11"}
]



def get_upcoming_birthdays (users: list) -> list:                                        # Function getting list of dictionaries
    output = [] 
    for person in users:
        birthday = person["birthday"]                                                    # Get birthday str
        birthday_date = datetime.strptime(birthday, "%Y.%m.%d")                          # converting to datetime obj
        today = datetime.today()
        current_year = today.year
        birthday_date = birthday_date.replace(year=current_year)                         # converting birth date to current year   
        diff = birthday_date - today
        
        if diff.days <= 7 and diff.days >= 0:                                            # Perform check diff <= 7 days to today                                              
            
            while birthday_date.weekday() >= 5:                                          # Calculate congratulation_date 
                birthday_date = birthday_date + timedelta(days=1)                        # go one plus day while holidays
            
            congr_date = birthday_date.strftime("%Y-%m-%d %H:%M")                        # Check if weekednd and
            output_dict = {"name": person["name"], "congratulation_date" : congr_date}   # add formated dict to output
            output.append(output_dict)
    return output


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)