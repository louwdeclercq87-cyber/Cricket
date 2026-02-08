class PlayerDatabase:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def get_all_players(self):
        return self.players

    def find_player(self, player_name):
        for player in self.players:
            if player['name'] == player_name:
                return player
        return None

# Example usage:
if __name__ == '__main__':
    db = PlayerDatabase()
    db.add_player({'name': 'John Doe', 'age': 30, 'team': 'A'})
    db.add_player({'name': 'Jane Smith', 'age': 25, 'team': 'B'})
    print(db.get_all_players())