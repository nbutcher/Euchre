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

def ShowPlay(cards):
    """Arranges played cards in an easy to read format for the player. If a
    computer controlled position has not yet played a card, this function
    expects them to have a string of XXX input. The indices are 0 for player,
    1 for left of player, 2 for partner, and 3 for right of player."""

    s1 = ' ' * 6 + cards[2].Show()
    s2 = cards[1].Show() + ' ' * 9 + cards[3].Show()
    s3 = ' ' * 6 + cards[0].Show()

    print(s1 + '\n')
    print(s2 + '\n')
    print(s3 + '\n')
    return

def FirstPassCall(pos,dealpos,hands,upcard,scores,aggro):
    """Function to call trump on the first pass (with upcard). Position is
    0 for player, 1 for left of player, 2 for partner, and 3 for right of 
    player. Upcard is what trump can be and the dealer will pick it up if 
    called. Scores is a 2 element list with [player, other] to allow the 
    computer to call trump more aggresively if the other team has 9 points
    or avoid inappropriate loner calls. This function will find a 'score' for
    how much it wants to call trump and will compare it to the aggresiveness
    set at the start. Returns a 1 to call and 0 to pass."""

    upsuit = upcard.GetSuit()
    uprank = upcard.GetRank()
    myhand = hands[pos]
    points = 0
    trump_count = 0
    crank = []
    csuit = []
    counts = {"S":0,"C":0,"H":0,"D":0}
    for c in myhand:
        crank.append(c.GetRank())
        csuit.append(c.GetSuit())
        counts[c.GetSuit()] += 1
    #print(counts)
    if (pos != dealpos and counts[upsuit] == 0):
        return 0
    
    for i in range(0,len(myhand)):
        if (csuit[i] == upsuit): #Would be trump
            if (crank == 11): #Jack
                points += 100.
            elif (crank == 14):
                points += 60.
            elif (crank == 13):
                points += 50.
            else:
                points += 35
       
        # Now check for left
        elif (myhand[i].SameColor(upcard) and crank == 11):
            points += 75
            
        
