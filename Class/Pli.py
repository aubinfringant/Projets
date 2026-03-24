import random

class Pli:

    def __init__(self):
        self.pli = []

    def result(self,j1,j2):
        if self.pli[-1].value < self.pli[-2].value:
            random.shuffle(self.pli)
            for i in range(len(self.pli)):
                j1.hand.append(self.pli[i])

        elif self.pli[-1].value > self.pli[-2].value:
            random.shuffle(self.pli)
            for i in range(len(self.pli)):
                j2.hand.append(self.pli[i])

        else:
            if len(j1.hand) > 1 and len(j2.hand) > 1:
                for i in range(2):
                    self.pli.append(j1.give_card())
                    self.pli.append(j2.give_card())
                return True

            else:
                for i in range(0,len(self.pli),2):
                    j1.hand.append(self.pli[i])
                    j2.hand.append(self.pli[i+1])

        return False
