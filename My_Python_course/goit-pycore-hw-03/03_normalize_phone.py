""" Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ 
'+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат,
 залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду,
 функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS. """
import re

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

def normalize_phone(phone_number: str) -> str:
    """
    Normalized phone number and returns "+380XXXXXXX" string

    Args:
        phone_number (str): Input phone number, may include spaces,
            parentheses, or dashes.

    Returns:
        str: Normalized phone number and returns "+380XXXXXXX" string
    """
    norm_number = ""
    for i in range(len(phone_number)):                                     # Iterating via position on string
        if phone_number[i].isdigit():            # Check True if it is digit
            norm_number += phone_number[i]       # Adding to result string 

    formating = "38"                          # State format to check add

    if norm_number[0:2] != formating:     # Condition for not international number do not match formatting excluding '+'
        norm_number = formating + norm_number
    norm_number = "+" + norm_number           # Adding + to all (isdigit removes it) 
    return norm_number                         

print(normalize_phone("+380 44 123 4567"))




sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)