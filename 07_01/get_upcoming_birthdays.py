from datetime import datetime, timedelta

# users = [
#     {"name": "John Doe", "birthday": "1985.03.18"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "Oksana Yahovkina", "birthday": "1987.02.28"},
#     {"name": "Dmytro Yahovkin", "birthday": "1989.03.19"}
# ]

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.now().date()
    date_interval = today + timedelta(days=7)
    
    for user in users:
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = datetime(today.year, birth_date.month, birth_date.day).date()
        day_of_week = congratulation_date.weekday()

        if congratulation_date < today:
            congratulation_date = datetime(today.year + 1, birth_date.month, birth_date.day).date()

        if today <= congratulation_date <= date_interval:
            if day_of_week == 5:
                congratulation_date += timedelta(days=2)
            elif day_of_week == 6:
                congratulation_date += timedelta(days=1)
            
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name":user["name"], "birthday": congratulation_date_str})
    
    return upcoming_birthdays

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)