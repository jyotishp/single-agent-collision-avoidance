from autograd import jacobian
from scipy.optimize import minimize, Bounds


class CollisionConstraint:
    def __init__(self, robot, obstacle):
        self.robot = robot
        self.obstacle = obstacle

    def constraint(self, control):
        return -1 * self.robot.get_collision_cone(self.obstacle, control)


class ReactivePlanner:
    def __init__(self, robot):
        self.robot = robot

    def desired_velocity_cost(self, control):
        desired_velocity = self.robot.get_desired_velocity()
        return sum((control - desired_velocity) ** 2)

    def aggressiveness_cost(self, control):
        return sum((self.robot.velocity - control) ** 2) * 0.3

    def get_cost(self, control):
        cost = self.desired_velocity_cost(control)
        cost += self.aggressiveness_cost(control)
        return cost

    def get_optimal_control(self, obstacles):
        initial_point = self.robot.velocity

        constraints = []
        for obstacle in obstacles:
            if not self.robot.is_colliding(obstacle):
                continue # skip if the obstacle is not in collision
            constraint = CollisionConstraint(self.robot, obstacle)
            constraints.append(
                {
                    "type": "ineq",
                    "fun": constraint.constraint,
                    "jac": jacobian(constraint.constraint),
                }
            )

        bounds = Bounds(
            [self.robot.velocity_lower_bound, self.robot.velocity_lower_bound],
            [self.robot.velocity_upper_bound, self.robot.velocity_upper_bound],
        )

        control = minimize(
            self.get_cost,
            x0=initial_point,
            method="SLSQP",
            constraints=constraints,
            options={"disp": False},
            bounds=bounds,
        )
        return control.x
