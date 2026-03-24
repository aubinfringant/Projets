class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []

    def give_card(self):
        return self.hand.pop()