from Card import Card
import random

class Deck:
    def __init__(self, ranks, suits):
        self.d = []
        for i in ranks:
            for j in suits:
                self.d.append(Card(i,j))

    def ShowDeck(self):
        for c in self.d:
            print(c.Show())

    def Shuffle(self):
        for i in range(0,int(1e3)):
            val = random.randint(1,len(self.d)-1)
            tempcard = self.d[val]
            self.d[val] = self.d[0]
            self.d[0] = tempcard

    def Draw(self):
        return self.d.pop()
