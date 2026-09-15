# Note : We can access to the class attrs using class name as below:

# Create a class with the name of Card to instantiate cards
class Card :
    
    #Class attrs
    suits = ['Clubs♣', 'Diamonds♦', 'Hearts♥', 'Spades♠']
    ranks = ['None', 'Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    #Define Card constructor(setter)
    def __init__(self, suit = 0, rank = 1):
        """
        Set the values of any Card object.

        Default value of suit: ♣Clubs --> 0
        Default value of rank:  Ace   --> 1
        """

        print('Called while Card instantitation')
        self.suit = suit
        self.rank = rank

        #Define Card printer(getter)
    def __str__(self):
            return f'{Card.ranks[self.rank]} of {Card.suits[self.suit]}'

    @classmethod
    def get_suits(cls):
            return cls.suits.copy()

    @classmethod
    def get_ranks(cls):
            return cls.ranks.copy()

    def compare(self, other):
        
            
        """
        1. Ace are lower than 2s.
        2. Suits are more singnificant than ranks.

        If suit of this card is greater than suit of that card : return 1
        If suit of that card is greater than suit of this card : return -1

        If suits are the same then :
        If rank of this card is greater than rank of that card : return 1
        If rank of that card is greater than rank of this card : return -1

        If ranks are the same, too: return 0
        """
            
        if other.suit > self.suit: return -1
        if other.suit < self.suit: return  1
        if other.rank > self.rank: return -1
        if other.rank < self.rank: return  1
        return 0


    def __gt__(self, other): return self.compare(other) > 0
    def __lt__(self, other): return self.compare(other) < 0
    def __ge__(self, other): return self.compare(other) >=0
    def __le__(self, other): return self.compare(other) <=0
    def __eq__(self, other): return self.compare(other) ==0
    def __ne__(self, other): return self.compare(other) !=0

### Driver Code for Card instantiations ###
c1 = Card()  #Ace of Clubs♣️ #__init__(self = c1, suit = 0, rank = 1)
c2 = Card(suit = 2, rank = 2) # 2 of Hearts♥
#c1, c2, c1.compare(c2)
#ranks_copy = c1.get_ranks()
#suits_copy = c1.get_suits()

#suits_copy
print(c1)
print(c2)
print('Comparison:' ,c1.compare(c2))
print(f'c1 < c2? {c1 and c2}')
