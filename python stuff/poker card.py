#suit is more important than the rank,
#and the suits are sorted as in Bridge: Spades, Hearts, Diamonds, Clubs.
#default card is 2 of Clubs
class Card:
    __doc__='''represents a playing card, to create give an int for suit and an int for rank
the ranks are 2-14 with Ace rank 14
the suits are 0-3 sorted: Clubs, Diamonds, Hearts, Spades
'''
    ranks=['0','1',"2",'3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suits=["Clubs", "Diamonds", "Hearts", "Spades"]
    def __init__(s,suit=0,rank=2):
        s.suit=suit
        s.rank=rank
    def __str__(s):
        return s.ranks[s.rank]+" of "+s.suits[s.suit]
    def __eq__(s, o):
        if s.rank==o.rank:
            if s.suit==o.suit:
                return True
        return False
    def __gt__(s,o):
        #s>o
        if s.suit>o.suit:
            return True
        if s.suit==o.suit:
            if s.rank>o.rank:
                return True
        return False
    def __lt__(s,o):
        #s<o
        if s.suit<o.suit:
            return True
        if s.suit==o.suit:
            if s.rank<o.rank:
                return True
        return False
