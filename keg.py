from useful import generate_number_not_used

class Keg:
    def __init__(self):
        self.number = 0

    def generate_number(self, cards_numbers, kegs_numbers_used):
        self.number = generate_number_not_used(cards_numbers, kegs_numbers_used)

