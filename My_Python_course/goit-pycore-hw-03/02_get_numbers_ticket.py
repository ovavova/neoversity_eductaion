""" Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і
 в певному діапазоні під час чергового тиражу.  Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел
для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні """

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:                # min >= 1; max <=1000; quantity 
    if min < 1 or max > 1000 or max < min or quantity < min or quantity > max :   # parameters check
        return "Please check parameters. min >= 1; max <=1000; quantity between min and max"  
    rndm_list = []
    i = 0
    while i < quantity:
        rnd_num = random.randint(min, max) # generating random number
        if rnd_num not in rndm_list:       # check if number is unique 
            rndm_list.append(rnd_num)      # adding to list if unique 
            i +=1                          # iterating
    rndm_list.sort()                       # sorting list
    return rndm_list

print(get_numbers_ticket(1,100,10))

    
