from useful import fill_list_numbers

class Card:
    def __init__(self, cards_numbers, cards_numbers_used):
        self.rows = 3
        self.columns = 9

        lst = []
        for row in range(1, 4):
            lst.append(fill_list_numbers(cards_numbers, cards_numbers_used))

        self.lst = lst

    def __str__(self):
        for lst_tmp in self.lst:
            print(lst_tmp)

        return ''

    def search_number(self, number_for_search):
        for lst_temp in self.lst:
            if number_for_search in lst_temp:
                return True
        return False

    def search_and_delete_number(self, number_for_search):
        for lst_temp in self.lst:
            if number_for_search in lst_temp:
                index_temp = lst_temp.index(number_for_search)
                lst_temp.pop(index_temp)
                lst_temp.insert(index_temp, '-')

                return True

        return False

    def check_card(self):
        for lst_temp in self.lst:
            for i in lst_temp:
                if not (i == 0 or i == '-'):
                    return False
        return True