# Pitch Characteristics and Conditions

class Pitch:
    def __init__(self, material, bounce, spin, condition):
        self.material = material  # Material of the pitch (e.g., grass, clay)
        self.bounce = bounce        # Average bounce height
        self.spin = spin            # Spin effect on the ball
        self.condition = condition  # Current condition (e.g., dry, wet)

    def describe(self):
        return (f"Pitch Material: {self.material}, Bounce: {self.bounce}, Spin: {self.spin}, "
                f"Condition: {self.condition}")

# Example usage
pitch = Pitch(material='Grass', bounce=0.30, spin='Moderate', condition='Dry')
print(pitch.describe())