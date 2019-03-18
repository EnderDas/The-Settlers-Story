from BlueDB.Blue2 import Blue

"""
TODO: make a solid framework for the players saving system
"""


class Player:

    def __init__(self, name):
        self.name = name
        self.inventory = None
        self.weapon = None
        self.armor = None
        
        # TODO: Work on metadata for position and etc
    
    @property
    def attack(self):
        # TODO: make an attack equation
        return 0
    
    @property
    def defense(self):
        # TODO: make a defense equation
        return 0

