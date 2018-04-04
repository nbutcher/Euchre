class Card:
    def __init__(self, rank, suit):
        self.r = rank
        self.s = suit

    def Show(self):
        if (self.r < 10):
            outr = ' ' + str(self.r)
        elif (self.r == 10):
            outr = str(self.r)
        elif (self.r == 11):
            outr = ' J'
        elif (self.r == 12):
            outr = ' Q'
        elif (self.r == 13):
            outr = ' K'
        elif (self.r == 14):
            outr = ' A'
        else:
            print("Rank Error")
        return outr + self.s

    def GetRank(self):
        return self.r
    def GetSuit(self):
        return self.s

