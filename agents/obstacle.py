from agents.agent import Agent


class Obstacle(Agent):
    def __init__(self, position, velocity, radius, goal, max_velocity=1):
        super().__init__(
            position=position,
            velocity=velocity,
            radius=radius,
            goal=goal,
            max_velocity=max_velocity,
        )

    def move(self):
        self.set_velocity(self.get_desired_velocity())
