import random

def generate_number_not_used(list_numbers, list_numbers_used):
    is_used = False
    while not is_used:
        number = random.choice(list_numbers)
        if number not in list_numbers_used:
            is_used = True

    list_numbers_used.append(number)

    return number


def find_free_place(lst_tmp):
    is_selected = False
    while not is_selected:
        index_random = random.choice(range(1, 10))
        if lst_tmp[index_random - 1] == 0:
            is_selected = True

    return index_random


def fill_list_numbers(cards_numbers, cards_numbers_used):
    lst_tmp = [0 for _ in range(1, 10)]
    for times in range(1, 6):
        number = generate_number_not_used(cards_numbers, cards_numbers_used)
        index_random = find_free_place(lst_tmp)

        lst_tmp.pop(index_random - 1)
        lst_tmp.insert(index_random - 1, number)

    return lst_tmp