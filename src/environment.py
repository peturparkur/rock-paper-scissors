

from copy import copy
import typing
from tqdm import tqdm
from src.agent import Agent

"""
0 -> Rock
1 -> Paper
2 -> Scissors
"""

class Environment():

    state : dict
    selection : typing.List[str] = ['Rock', 'Paper', 'Scissors']
    turn_choices : typing.Dict[str, int] = {
                                            'Rock' : 0,
                                            'Paper' : 1,
                                            'Scissors' : 2}

    def __init__(self, N : int = 1000) -> None:

        self.state = {'turn' : 0, 'max_turn' : N,
                    'outcome' : -1, 
                    'p1' : -1, 'p2' : -1,
                    'p1_score' : 0, 'p2_score' : 0,
                    'draws' : 0,
                    }
        self.state['constants'] = self.Constants
        pass
    
    def reset(self):
        self.state = {'turn' : 0, 'max_turn' : self.state['max_turn'],
                    'outcome' : -1, 
                    'p1' : -1, 'p2' : -1,
                    'p1_score' : 0, 'p2_score' : 0,
                    'draws' : 0,
                    }
        self.state['constants'] = self.Constants
        return self

    @property
    def Constants(self):
        return {
            'Selection' : self.selection,
            'Choices' : self.turn_choices
        }

    def turn(self, player1 : Agent, player2 : Agent):
        p1_state = copy(self.state)
        p1_state['player'] = 'p1'
        p1 = player1.turn(p1_state)
        p2_state = copy(self.state)
        p2_state['player'] = 'p2'
        p2 = player2.turn(p2_state)
        x = p1 - p2 # The difference of options

        y = x % 3 # to see easy way the winner / loser
        # 0 -> draw
        # 1 -> p1 win
        # 2 -> p2 win
        self.state['p1'] = p1
        self.state['p2'] = p2
        self.state['turn'] += 1
        self.state['outcome'] = y
        if(y == 1):
            self.state['p1_score'] += 1
        if(y == 2):
            self.state['p2_score'] += 1
        if(y == 0):
            self.state['draws'] += 1
        return self
    
    @property
    def prettify(self):
        """
        Make state pretty
        """
        s = copy(self.state)
        if s['outcome'] == 0:
            s['outcome'] = 'draw'
        if s['outcome'] == 1:
            s['outcome'] = 'p1 win'
        if s['outcome'] == 2:
            s['outcome'] = 'p2 win'
        
        s['p1'] = self.selection[s['p1']]
        s['p2'] = self.selection[s['p2']]
        return s

    def play(self, player1 : Agent, player2 : Agent, verbose : bool = False):
        turns = []
        iterator = range(self.state['max_turn'])
        if verbose: iterator = tqdm(iterator)
        for i in iterator:
            turns.append(self.turn(player1, player2).prettify)
        return turns

    pass