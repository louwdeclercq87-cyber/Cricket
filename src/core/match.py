class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.scoreboard = {team1: 0, team2: 0}
        self.overs = 0
    
    def simulate_over(self):
        import random
        runs = random.randint(0, 6)  # simulate runs for an over
        batting_team = self.team1 if self.overs % 2 == 0 else self.team2
        self.scoreboard[batting_team] += runs
        self.overs += 1
        return runs

    def play(self, total_overs):
        for _ in range(total_overs):
            runs = self.simulate_over()
            print(f"Over {self.overs}: {runs} runs scored by {self.team1 if self.overs % 2 == 0 else self.team2}")
        print(f"Final Score: {self.team1} {self.scoreboard[self.team1]} - {self.team2} {self.scoreboard[self.team2]}")

# Example usage:
# match = Match('Team A', 'Team B')
# match.play(5)