import Card
import Deck
a = Card.Card(2,'C')
b = Card.Card(12,'S')
c = Card.Card(10,'H')

a.Show()
b.Show()
c.Show()

print(a.GetRank())
print(a.GetSuit())

ranks = [9,10,11,12,13,14]
suits = ['C','H','S','D']

edeck = Deck.Deck(ranks,suits)
print(edeck.d)
