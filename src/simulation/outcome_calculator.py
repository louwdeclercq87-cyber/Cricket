import random

class OutcomeCalculator:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def calculate_outcome(self):
        outcome = random.choices(list(self.probabilities.keys()), weights=self.probabilities.values())[0]
        return outcome

# Probability distribution for possible outcomes
# This can be modified as needed
probabilities = {
    'Wicket': 0.1,
    'Run': 0.3,
    'No Ball': 0.05,
    'Wide': 0.05,
    'Dot Ball': 0.5
}

if __name__ == "__main__":
    calculator = OutcomeCalculator(probabilities)
    result = calculator.calculate_outcome()
    print(f"Outcome: {result}")