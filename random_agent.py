import typing
import random
from src.agent import Agent

class RandomAgent(Agent):
    def __init__(self, probs : typing.List[int] = [0.333, 0.333, 0.333]) -> None:
        p = sum(probs)
        self.p = [x / p for x in probs]

    def turn(self, state : dict):
        return random.choices(range(3), self.p)[0]
        # return np.random.choice(3, 1, p = self.p)