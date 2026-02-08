import random

class Ball:
    def __init__(self, bowler, batsman):
        self.bowler = bowler
        self.batsman = batsman
        self.result = None

    def simulate(self):
        # Randomly determine the outcome of the ball
        outcome = random.choice(['dot', '1', '2', '3', '4', '6', 'W'])
        self.result = outcome
        return outcome

class Over:
    def __init__(self, bowler, batsman):
        self.balls = []
        self.bowler = bowler
        self.batsman = batsman

    def bowl_ball(self):
        ball = Ball(self.bowler, self.batsman)
        outcome = ball.simulate()
        self.balls.append(outcome)
        return outcome

class Innings:
    def __init__(self, batting_team):
        self.batting_team = batting_team
        self.score = 0
        self.wickets = 0

    def bowl_over(self):
        over = Over(bowler='Bowler A', batsman='Batsman A')  # Use actual players
        for _ in range(6):  # Simulate 6 balls
            outcome = over.bowl_ball()
            if outcome == 'W':
                self.wickets += 1
                print(f'Wicket! {over.batsman} is out.')
            else:
                runs = int(outcome)  # Convert outcome to runs
                self.score += runs
                print(f'Runs: {runs}')
        print(f'End of Over - Score: {self.score}/{self.wickets}')

# Sample usage
innings = Innings(batting_team='Team A')
for _ in range(20):  # simulate 20 overs
    innings.bowl_over()
print(f'Total Score: {innings.score}/{innings.wickets}')