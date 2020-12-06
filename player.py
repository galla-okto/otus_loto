class Player:
    def __init__(self, index, is_man=True):
        self.index = index
        self.is_man = is_man
        self.loser = False
        self.winner = False
