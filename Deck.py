from Card import Card

class Deck:
    def __init__(self, ranks, suits):
        self.d = []
        for i in ranks:
            for j in suits:
                self.d.append(Card(i,j))


    
