import random

col_B = list(range(1,16))
col_I = list(range(16, 31))
col_N = list(range(31, 46))
col_G = list(range(46, 61))
col_O = list(range(61, 76))

# seed = random.randint(1,99999)
# seed = 96011
# random.seed(seed)
# random.shuffle(col_B)
#
#
#
# print(f'\n{col_B}, seed = {seed}')
# print(f"{1:05d}")

class BingoCard():

    def __init__(self):
        self.card_seed = random.randint(1,99999)
        self.cols = (col_B, col_I, col_N, col_G, col_O)
        self.randomise_card()

    def randomise_card(self):
        random.seed(self.card_seed)
        for col in self.cols:
            random.shuffle(col)

# card1 = BingoCard()
# #
# print(f"{card1.card_seed:05d}, col_B: {sorted(card1.cols[0])}")
# print(f"{card1.card_seed:05d}, col_B: {sorted(card1.cols[1])}")
# print(f"{card1.card_seed:05d}, col_B: {sorted(card1.cols[2])}")
# print(f"{card1.card_seed:05d}, col_B: {sorted(card1.cols[3])}")
# print(f"{card1.card_seed:05d}, col_B: {sorted(card1.cols[4])}")