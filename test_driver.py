import Card
import Deck
from Functions import Deal,ShowHand,ShowPlay,FirstPassCall

a = Card.Card(2,'C')
b = Card.Card(12,'S')
c = Card.Card(10,'H')

print(a.Show())
print(b.Show())
print(c.Show())

print(a.GetRank())
print(a.GetSuit())

ranks = [9,10,11,12,13,14]
suits = ['C','H','S','D']

edeck = Deck.Deck(ranks,suits)
edeck.ShowDeck()
print('Now to shuffle')
edeck.Shuffle()
edeck.ShowDeck()
print("Time to deal cards")
hands, upcard = Deal(edeck)
print(upcard.Show())
for i in hands:
    print(ShowHand(i))
print("Call test\n")
FirstPassCall(1,1,hands,upcard,[0,0],0)
