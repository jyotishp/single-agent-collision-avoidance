import numpy as np
import matplotlib.pyplot as plt


def plot_simulation(robot, obstacles):
    plt.clf()
    ax = plt.gcf().gca()
    ax.set_xlim((-1, 11))
    ax.set_ylim((-1, 11))

    plot_robot(ax, robot)
    plot_obstacles(ax, obstacles)


def plot_robot(ax, robot):
    color = "#059efb"
    ax.add_artist(
        plt.Circle(robot.position, robot.sensor_range, color="gray", alpha=0.1)
    )
    plot_circle(ax, color, robot, zorder=100)
    plot_path(color, robot)


def plot_obstacles(ax, obstacles):
    for obstacle in obstacles:
        plot_circle(ax, "#ffa804", obstacle)


def plot_circle(ax, color, agent, zorder=20):
    ax.add_artist(
        plt.Circle(
            agent.position,
            agent.radius,
            facecolor=color,
            edgecolor="black",
            zorder=zorder,
        )
    )


def plot_path(color, robot):
    path = np.array(robot.path)
    plt.plot(path[:, 0], path[:, 1], color, zorder=1)
