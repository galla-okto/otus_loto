from card import Card
from player import Player
from keg import Keg

cards_numbers = [item for item in range(1, 91)]
cards_numbers_used = []
kegs_numbers_used = []

def generate_players_cards(number_players, list_players_cards, pc_man=True):
    index_start = len(list_players_cards)
    if number_players != 0:
        for item in range(1, number_players + 1):
            player = Player(index_start + item, pc_man)
            card = Card(cards_numbers, cards_numbers_used)
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
        keg.generate_number(cards_numbers, kegs_numbers_used)
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
