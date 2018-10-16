import random
from constants import roulette_place_map, bet_type_magnification_map


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

    def create(self, bet_type):
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
        roulette_place_list = RoulettePlaceListFactory().create(bet_type)
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
