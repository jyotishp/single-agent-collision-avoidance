import numpy as np
import matplotlib.pyplot as plt
from agents.robot import Robot
from agents.obstacle import Obstacle
from planner.reactive_planner import ReactivePlanner
from utils.plotting import plot_simulation


def main():
    robot = Robot(
        position=np.zeros(2),
        velocity=np.zeros(2),
        goal=np.array([10, 10]),
        radius=0.5,
        velocity_lower_bound=-1,
        velocity_upper_bound=1,
    )
    obstacles = [
        Obstacle(
            position=np.array([10, 10]),
            velocity=np.zeros(2),
            goal=np.array([0, 0]),
            radius=0.5,
        )
    ]
    planner = ReactivePlanner(robot=robot)

    while not robot.goal_reached():
        detected_obstacles = []
        for obstacle in obstacles:
            if robot.in_sensor_range(obstacle):
                detected_obstacles.append(obstacle)

        # Move the robot
        control = planner.get_optimal_control(detected_obstacles)
        robot.set_velocity(control)

        # Move the obstacles
        for obstacle in obstacles:
            obstacle.move()

        plot_simulation(robot, obstacles)
        plt.pause(1 / 10)
    plt.show() # prevent exiting until plotting window is closed


if __name__ == "__main__":
    main()
