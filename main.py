import random

cards_numbers = [item for item in range(1, 91)]
cards_numbers_used = []
kegs_numbers_used = []

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

def fill_list_numbers():
    lst_tmp = [0 for _ in range(1, 10)]
    for times in range(1, 6):
        number = generate_number_not_used(cards_numbers, cards_numbers_used)
        index_random = find_free_place(lst_tmp)

        lst_tmp.pop(index_random - 1)
        lst_tmp.insert(index_random - 1, number)

    return lst_tmp


class Player:
    def __init__(self, index, is_man=True):
        self.index = index
        self.is_man = is_man
        self.loser = False
        self.winner = False


class Card:
    def __init__(self):
        self.rows = 3
        self.columns = 9

        lst = []
        for row in range(1, 4):
            lst.append(fill_list_numbers())

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


class Keg:
    def __init__(self):
        self.number = 0

    def generate_number(self):
        self.number = generate_number_not_used(cards_numbers, kegs_numbers_used)

def generate_players_cards(number_players, list_players_cards, pc_man = True):
    index_start = len(list_players_cards)
    if number_players != 0:
        for item in range(1, number_players + 1):
            player = Player(index_start + item, pc_man)
            card = Card()
            list_players_cards.append((player, card))

if __name__ == '__main__':
    number_player_pc = int(input('Enter quantity of computer players: '))
    number_player_man = int(input('Enter quantity of man players: '))

    list_players_cards = []

    generate_players_cards(number_player_pc, list_players_cards, False)
    generate_players_cards(number_player_man, list_players_cards)

    keg = Keg()

    game_is_over = False
    while not game_is_over:
        keg.generate_number()
        number_tmp = keg.number
        print('New keg = ', number_tmp, ' (left ', (90 - len(kegs_numbers_used)), ')')

        for player_card_tmp in list_players_cards:
            player_tmp = player_card_tmp[0]
            card_tmp = player_card_tmp[1]

            print('Card of ', 'man' if player_tmp.is_man else 'computer',  ' Nr', player_tmp.index)
            print(card_tmp)
            print('---------------------------------')

        for player_card_tmp in list_players_cards:
            player_tmp = player_card_tmp[0]
            card_tmp = player_card_tmp[1]

            if player_tmp.is_man:
                answer = input(f'Question for player Nr {player_tmp.index}: Cross out the number? (y/n)')

                if answer == 'y':
                    if card_tmp.search_number(number_tmp):
                        card_tmp.search_and_delete_number(number_tmp)
                    else:
                        player_tmp.loser = True
                        game_is_over = True
                        print('Lose player Nr ', player_tmp.index)
                        break
                else:
                    if card_tmp.search_number(number_tmp):
                        player_tmp.loser = True
                        game_is_over = True
                        print('Lose player Nr ', player_tmp.index)
                        break
            else:
                card_tmp.search_and_delete_number(number_tmp)

            if card_tmp.check_card():
                player_tmp.winner = True
                game_is_over = True
                print('Win player Nr ', player_tmp.index)
                break
