from roulette import RouletteGame


def select_game(game_type):
    if game_type in ['roulette']:
        return RouletteGame
    ValueError(f'game type is invalid. given {game_type}')


class MartinGale:
    def __init__(self, funds, game_type, initial_bet, simulation_num=1000):
        self.funds = funds
        self.funds_log = []
        self.initial_bet = initial_bet
        self.game_class = select_game(game_type)
        self.simulation_num = simulation_num

    def simulate(self):
        bet = self.initial_bet
        for i in range(self.simulation_num):
            bet = bet if bet < self.funds else self.funds

            self.funds -= bet
            refund = self.play(bet)

            if refund > 0:
                bet = self.initial_bet
                self.funds += refund
            else:
                bet = bet * 2
            self.funds_log.append(self.funds)

            if self.funds <= 0:
                break
        return self.funds_log

    def play(self, bet):
        # TODO: enable to bet other games and  bet_type
        game = self.game_class(bet, 'red')
        return game.play()
