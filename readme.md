# Single agent collision avoidance

This code implements collision avoidance using velocity obstacles. Collision avoidance constraints are expressed as polynomial inequalities and solved using [`SLSQP`](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html).

## Initial Setup

```bash
pip install -r requirements.txt
```

## Running the code

```bash
python main.py
```

## Running for multiple obstacles

You can add more obstacles in the [`main.py`](main.py#L18).

For example,

```python
import numpy as np
from agents.obstacle import Obstacle

obstacles = [
    Obstacle(
        position=np.array([10, 10]),
        velocity=np.zeros(2),
        goal=np.array([0, 0]),
        radius=0.5,
    ),
    Obstacle(
        position=np.array([10, 0]),
        velocity=np.zeros(2),
        goal=np.array([0, 10]),
        radius=0.5,
    ),
]
```
