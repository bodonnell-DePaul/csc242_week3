from Card import Card
from random import shuffle as random_shuffle
class Deck:
    'represents a deck of 52 cards'
    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty
        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))
    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop(0)
    def shuffle(self):
        'shuffle the deck'
        random_shuffle(self.deck)

    def __str__(self):
        retVal = ""
        for card in self.deck:
            retVal += str(card)+'\n'
        return retVal#"{}".format(self.deck)


    def __repr__(self):
        retVal = ""
        for card in self.deck:
            retVal += str(card)+'\n'
        return retVal#"{}".format(self.deck)
