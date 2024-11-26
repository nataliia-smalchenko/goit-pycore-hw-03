import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Функція повертає випадковий набір чисел кількістю quantity у межах від min до max. 
    Усі випадкові числа в наборі унікальні.
    """
    if min < 1 or min > 1000: return []
    if max > 1000 or max < min: return []
    if quantity > max - min: return []
    numbers_ticket = random.sample(range(min, max + 1), quantity)
    return sorted(numbers_ticket)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)