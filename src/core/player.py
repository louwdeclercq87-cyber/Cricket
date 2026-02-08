class Player:
    def __init__(self, name, age, team, runs=0, wickets=0):
        self.name = name
        self.age = age
        self.team = team
        self.runs = runs
        self.wickets = wickets

    def score_run(self, runs):
        self.runs += runs

    def take_wicket(self):
        self.wickets += 1

    def __str__(self):
        return f'{self.name} (Age: {self.age}) - Team: {self.team}, Runs: {self.runs}, Wickets: {self.wickets}'
