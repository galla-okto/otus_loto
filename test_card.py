from card import Card


class TestCardSearchNumber:
    def test_return_type_search_number(self):
        cards_numbers = [item for item in range(1, 91)]
        cards_numbers_used = []

        card_tmp = Card(cards_numbers, cards_numbers_used)
        number_for_search = 5
        res = card_tmp.search_number(number_for_search)
        assert isinstance(res, bool)

    def test_return_search_number(self):
        cards_numbers = [item for item in range(1, 16)]
        cards_numbers_used = []

        card_tmp = Card(cards_numbers, cards_numbers_used)
        number_for_search = 5
        res = card_tmp.search_number(number_for_search)
        assert res == True

class TestCardCheckCard:
    def test_return_check_card(self):
        cards_numbers = [item for item in range(1, 16)]
        cards_numbers_used = []

        card_tmp = Card(cards_numbers, cards_numbers_used)
        res = card_tmp.check_card()
        assert res == False