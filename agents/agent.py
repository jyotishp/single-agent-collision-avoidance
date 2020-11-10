import numpy as np


class Agent:
    def __init__(self, position, velocity, radius, goal, max_velocity=1):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.goal = goal
        self.max_velocity = max_velocity
        self.path = []
        self.dt = 0.1
        self.goal_tolerance = 0.1

    def set_velocity(self, velocity):
        self.position = self.position + velocity * self.dt
        self.velocity = velocity
        self.path.append(self.position)

    def get_desired_velocity(self):
        vector = self.goal - self.position
        desired_velocity = vector * self.max_velocity / np.sqrt(sum(vector ** 2))
        # Slow the agent as it approaches the goal
        goal_distance = sum(vector ** 2)
        if goal_distance < 1:
            return desired_velocity * goal_distance
        return desired_velocity

    def goal_reached(self):
        return sum((self.position - self.goal) ** 2) < self.goal_tolerance ** 2
