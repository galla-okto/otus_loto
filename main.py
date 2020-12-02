import random

cards_numbers = [item for item in range(1, 91)]
cards_numbers_used = []
kegs_numbers_used = []


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
            lst_tmp = [0 for _ in range(1, 10)]
            for times in range(1, 6):
                is_used = False
                while not is_used:
                    number = random.choice(cards_numbers)
                    if number not in cards_numbers_used:
                        is_used = True

                cards_numbers_used.append(number)

                is_selected = False
                while not is_selected:
                    index_random = random.choice(range(1, 10))
                    if lst_tmp[index_random - 1] == 0:
                        is_selected = True

                lst_tmp.pop(index_random - 1)
                lst_tmp.insert(index_random - 1, number)

            lst.append(lst_tmp)

        self.lst = lst

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
        is_used = False
        while not is_used:
            number = random.choice(cards_numbers)
            if number not in kegs_numbers_used:
                is_used = True

        kegs_numbers_used.append(number)
        self.number = number


if __name__ == '__main__':
    number_player_pc = int(input('Enter quantity of computer players: '))
    number_player_man = int(input('Enter quantity of man players: '))

    list_players_cards = []

    if number_player_pc != 0:
        for item in range(1, number_player_pc + 1):
            player = Player(item, False)
            card = Card()
            list_players_cards.append((player, card))

    if number_player_man != 0:
        for item in range(1, number_player_man + 1):
            player = Player(number_player_pc + item)
            card = Card()
            list_players_cards.append((player, card))

    keg = Keg()

    game_is_over = False
    while not game_is_over:
        keg.generate_number()
        number_tmp = keg.number
        print('New keg = ', number_tmp, ' (left ', (90 - len(kegs_numbers_used)), ')')

        for player_tmp in list_players_cards:
            if player_tmp[0].is_man:
                print('Card of player Nr', player_tmp[0].index)
                for lst1 in player_tmp[1].lst:
                    print(lst1)
                print('---------------------------------')
            else:
                print('Card of computer Nr', player_tmp[0].index)
                for lst1 in player_tmp[1].lst:
                    print(lst1)
                print('---------------------------------')

        for player_tmp in list_players_cards:
            if player_tmp[0].is_man:
                answer = input(f'Question for player Nr {player_tmp[0].index}: Cross out the number? (y/n)')

                if answer == 'y':
                    if player_tmp[1].search_number(number_tmp):
                        player_tmp[1].search_and_delete_number(number_tmp)
                    else:
                        player_tmp[0].loser = True
                        game_is_over = True
                        print('Lose player Nr ', player_tmp[0].index)
                        break
                else:
                    if player_tmp[1].search_number(number_tmp):
                        player_tmp[0].loser = True
                        game_is_over = True
                        print('Lose player Nr ', player_tmp[0].index)
                        break
            else:
                player_tmp[1].search_and_delete_number(number_tmp)

            if player_tmp[1].check_card():
                player_tmp[0].winner = True
                game_is_over = True
                print('Win player Nr ', player_tmp[0].index)
                break
