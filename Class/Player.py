class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []

    def drop(self):
        return self.hand.pop(0)