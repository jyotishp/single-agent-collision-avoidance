import numpy as np
from agents.robot import Robot
from agents.obstacle import Obstacle


def test_is_colliding():
    robot = Robot(
        position=np.array([0, 0]),
        velocity=np.array([1, 1]),
        goal=np.array([10, 10]),
        radius=1,
        velocity_lower_bound=-1,
        velocity_upper_bound=1,
    )
    obstacle = Obstacle(
        position=np.array([10, 10]),
        velocity=np.array([-1, -1]),
        goal=np.array([0, 0]),
        radius=1,
    )
    assert robot.is_colliding(obstacle)

    # Non colliding case
    obstacle.velocity = np.array([1, 1])
    assert not robot.is_colliding(obstacle)
