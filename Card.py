class Card:
    'represents a playing card'
    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit
    def getRank(self):
        'return rank'
        return self.rank
    def getSuit(self):
        'return suit'
        return self.suit 
    
    def __str__(self):
        return "({},{})\n".format(self.getSuit(), self.getRank())


    def __repr__(self):
        return "({},{})\n".format(self.getSuit(), self.getRank())
