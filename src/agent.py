
class Agent:
    """
    Base Agent for interface with Rock-Paper-Scissors environment
    """
    def turn(self, state : dict):
        """
        Called at every turn of rock-paper-scissors

        Params
        ------
        @state: The current environment status as JSON / Dictionary

        Returns
        ------
        @int: number between [0, 3) which represents (Rock, Paper, Scissors)
        """
        pass