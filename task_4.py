from datetime import datetime, timedelta, date
import calendar

def get_nearest_congratulation_day(user_birthday, today):
    # check if birthday is February 29
    if calendar.isleap(user_birthday.year) and user_birthday.month == 2 \
                    and user_birthday.day == 29:
        if calendar.isleap(today.year):
            nearest_user_birthday = date(today.year, user_birthday.month, user_birthday.day)
            if nearest_user_birthday < today:
                nearest_user_birthday = date(today.year + 1, 3, 1)
        else:
            nearest_user_birthday = date(today.year, 3, 1)
            if nearest_user_birthday < today:
                if calendar.isleap(nearest_user_birthday.year):
                    nearest_user_birthday = date(today.year + 1, user_birthday.month, user_birthday.day)
                else:
                    nearest_user_birthday = date(today.year + 1, 3, 1)
    else:
        # birthday is not February 29
        nearest_user_birthday = date(today.year, user_birthday.month, user_birthday.day)
        if nearest_user_birthday < today:
            nearest_user_birthday = date(today.year + 1, user_birthday.month, user_birthday.day)

    # shift congratulation day to workday
    if user_birthday.weekday == 5:
        congratulation_day = nearest_user_birthday + timedelta(days=2)
    elif user_birthday.weekday == 6:
        congratulation_day = nearest_user_birthday + timedelta(days=1)
    else:
        congratulation_day = nearest_user_birthday

    # return
    return congratulation_day

def get_upcoming_birthdays(users):
    refined_users = []
    today = datetime.today().date()
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_day = get_nearest_congratulation_day(user_birthday, today)

        # Interval from today to user birthday
        days_to_birthday = (congratulation_day - today).days
        if days_to_birthday <= 7:
            str_congratulation_day = congratulation_day.strftime("%Y.%m.%d")
            refined_users.append({"name": user["name"], "congratulation_date": str_congratulation_day})
            
    return refined_users

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Smith", "birthday": "1985.11.23"},
    {"name": "Jane Doe", "birthday": "1999.11.26"},
    {"name": "Anna Doe", "birthday": "2003.12.01"},
    {"name": "Kelly Doe", "birthday": "2000.02.29"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)