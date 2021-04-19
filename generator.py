import random
from copy import deepcopy




class BingoCard():

    col_B = list(range(1, 16))
    col_I = list(range(16, 31))
    col_N = list(range(31, 46))
    col_G = list(range(46, 61))
    col_O = list(range(61, 76))

    cols = (col_B, col_I, col_N, col_G, col_O)

    def __init__(self):
        self.card_seed = random.randint(1,99999)
        self.cols = self._randomise_card(self.card_seed)

    @classmethod
    def _randomise_card(cls, seed):
        random.seed(seed)
        asd = deepcopy(cls.cols)
        for col in asd:
            random.shuffle(col)

        return asd