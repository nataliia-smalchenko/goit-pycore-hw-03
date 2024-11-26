import re

# Найпростіше рішення
def normalize_phone(phone_number):
    pattern = r"\D"
    cleared_number = re.sub(pattern, "", phone_number)
    if len(cleared_number) == 12:
        return "+" + cleared_number
    if len(cleared_number) == 10:
        return "+38" + cleared_number

# Рішення, що відповідає крокам із завдання 
def normalize_phone_2(phone_number):
    pattern = r"[^0-9+]"
    cleared_number = re.sub(pattern, "", phone_number)
    if cleared_number.startswith("+380"):
        return cleared_number
    if cleared_number.startswith("380"):
        return "+" + cleared_number
    if len(cleared_number) == 10:
        return "+38" + cleared_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

sanitized_numbers = [normalize_phone_2(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)