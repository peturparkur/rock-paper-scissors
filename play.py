from src.environment import Environment
from rock import SimpleAgent
from random_agent import RandomAgent

# a1 = SimpleAgent(0)
# a2 = SimpleAgent(1)

a1 = RandomAgent()
a2 = RandomAgent()

env = Environment(10000)
t = env.play(a1, a2, True)
print(t[0])
print(t[-1])