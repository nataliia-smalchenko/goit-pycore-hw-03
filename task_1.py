from datetime import datetime


def get_days_from_today(date: str):
    """
    Функція розраховує кількість днів між заданою датою і поточною датою. 
    Параметр date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
    """
    now_date = datetime.today()
    try:
        received_date = datetime.strptime(date, "%Y-%m-%d")
        difference = now_date - received_date
        return difference.days
    except Exception:
        print("Incorrect input data")


print("Днів від 9 жовтня 2021 року:", get_days_from_today("2021-10-09"))
print("Днів від 9 листопада 2024 року:", get_days_from_today("2024-11-09"))
print("Днів від 30 листопада 2024 року:", get_days_from_today("2024-11-30"))
print("Днів від 31 грудня 2024 року:", get_days_from_today("2024-12-31"))
print("Днів від неправильної дати:", get_days_from_today("-202-12-31"))