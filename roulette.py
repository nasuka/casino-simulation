import random

# TODO: extend other bet types
bet_type_magnification_map = {
    'black': 2,
    'red': 2,
    'odd': 2,
    'even': 2
}

roulette_place_map = {
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'black',
    12: 'red',
    13: 'black',
    14: 'red',
    15: 'black',
    16: 'red',
    17: 'black',
    18: 'red',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'black',
    30: 'red',
    31: 'black',
    32: 'red',
    33: 'black',
    34: 'red',
    35: 'black',
    36: 'red',
    0: 'green',
}

class RoulettePlace:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    @property
    def is_even(self):
        return self.number % 2 == 0

    @property
    def is_odd(self):
        return not self.is_even

    @property
    def is_red(self):
        return self.color == 'red'

    @property
    def is_black(self):
        return self.color == 'black'

class RoulettePlaceList:
    def __init__(self, items):
        self.items = items


class RoulettePlaceListFactory:
    all_roulette_place_list = [RoulettePlace(number, color) for number, color in roulette_place_map.items()]
    bet_type_list = ['black', 'red', 'odd', 'even']

    def create_place_list(self, bet_type):
        if bet_type == 'black':
            return RoulettePlaceList([roulette_place for roulette_place in self.all_roulette_place_list
                                      if roulette_place.is_black])
        elif bet_type == 'red':
            return RoulettePlaceList([roulette_place for roulette_place in self.all_roulette_place_list
                                      if roulette_place.is_red])
        elif bet_type == 'even':
            return RoulettePlaceList([roulette_place for roulette_place in self.all_roulette_place_list
                                      if roulette_place.is_even])
        elif bet_type == 'odd':
            return RoulettePlaceList([roulette_place for roulette_place in self.all_roulette_place_list
                                      if roulette_place.is_odd])

        valid_bet_types = ','.join(self.bet_type_list)
        ValueError(f'bet type is invalid. given bet_type is {bet_type}, but bet type should be {valid_bet_types}')


class RouletteBetFactory:
    bet_type_magnification_map = bet_type_magnification_map

    def create(self, bet, bet_type):
        assert bet_type in self.bet_type_magnification_map
        magnification = self.bet_type_magnification_map[bet_type]
        roulette_place_list = RoulettePlaceListFactory().create_place_list(bet_type)
        return RouletteBet(bet, magnification, roulette_place_list)


class RouletteBet:
    def __init__(self, bet, magnification, roulette_place_list):
        self.bet = bet
        self.magnification = magnification
        self.roulette_place_list = roulette_place_list

    def is_number_included(self, number):
        return any(number == roulette_place.number for roulette_place in self.roulette_place_list.items)

    def play(self, sampled_roulette_place):
        is_win = self.is_number_included(sampled_roulette_place.number)
        if is_win:
            return self.bet * self.magnification
        return 0


class RouletteGame:
    # TODO: allow multiple bet
    def __init__(self, bet, bet_type):
        self.roulette_bet = RouletteBetFactory().create(bet, bet_type)

    def play(self):
        sampled_roulette_place = random.choice(RoulettePlaceListFactory.all_roulette_place_list)
        return self.roulette_bet.play(sampled_roulette_place)

game = RouletteGame(100, 'red')
