import random

class SquadSelector:
    def __init__(self, players, squad_size):
        self.players = players
        self.squad_size = squad_size

    def select_squad(self):
        selected_squad = random.sample(self.players, self.squad_size)
        return selected_squad

if __name__ == '__main__':
    players_list = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 
                   'Player6', 'Player7', 'Player8', 'Player9', 'Player10']
    squad_size = 11
    selector = SquadSelector(players_list, squad_size)
    squad = selector.select_squad()
    print(f'Selected Squad: {squad}')