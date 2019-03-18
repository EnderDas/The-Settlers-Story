from BlueDB.Blue2 import Blue
"""
TODO: complete inventory class to work hand in hand with forge and shop
"""

class Inventory:
    
    def __init__(self, player):
        # TODO: should load everything from BlueDB
        self.player = player
        self.weapons = []
        self.armors = []
        self.items = []

        # Money and stuff

        self.money = 0