from agents.agent import Agent


class Robot(Agent):
    def __init__(
        self,
        position,
        velocity,
        radius,
        goal,
        velocity_lower_bound,
        velocity_upper_bound,
        max_velocity=1,
        sensor_range=5,
    ):
        # Pass the values to agent class
        super().__init__(
            position=position,
            velocity=velocity,
            radius=radius,
            goal=goal,
            max_velocity=max_velocity,
        )

        self.velocity_lower_bound = velocity_lower_bound
        self.velocity_upper_bound = velocity_upper_bound
        self.sensor_range = sensor_range

    def in_sensor_range(self, obstacle):
        return sum((self.position - obstacle.position) ** 2) < self.sensor_range ** 2

    def is_colliding(self, obstacle):
        if self.get_collision_cone(obstacle, self.velocity) <= 0:
            return False
        return True

    def get_collision_cone(self, obstacle, control):
        r = (
            self.position
            + control * self.dt
            - obstacle.position
            + obstacle.velocity * self.dt
        )
        v = control - obstacle.velocity
        if r.T @ v >= 0:
            return 0
        return (
            ((r.T @ v) ** 2)
            - sum(v ** 2) * sum(r ** 2)
            + sum(v ** 2) * (self.radius + obstacle.radius) ** 2
        )
