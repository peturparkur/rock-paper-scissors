

from src.agent import Agent


## Assume that:
"""
0 -> Rock
1 -> Paper
2 -> Scissors
"""

class RockAgent(Agent):
    def turn(self, state : dict):
        return 0

class SimpleAgent(Agent):
    def __init__(self, c : int = 0) -> None:
        self.c = c

    def turn(self, state : dict):
        return self.c