from Card import Card
from Deck import Deck

def Deal(edeck):
    """h1, h2, h3, h4 are the hands in order of who receives cards in the 
    deal. Should be empty lists. edeck is the euchre deck. This function
    sets up all hands and turns up a card."""
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    for i in range(0,5):
        h1.append(edeck.Draw())
        h2.append(edeck.Draw())
        h3.append(edeck.Draw())
        h4.append(edeck.Draw())
    upcard = edeck.Draw()
    return [h1,h2,h3,h4],upcard

def ShowHand(hand):
    outstr = ''
    for i in hand:
        outstr += i.Show()
    return outstr
