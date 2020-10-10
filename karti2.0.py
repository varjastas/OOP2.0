class Card:
    ''' Одна игральная карта. '''
    
    RANKS = ['Т', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'В', 'Д', 'K']
    # ♠ ♣ ♥ ♦
    SUITS = ['\u2660', '\u2663', '\u2665', '\u2666' ] 
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
    
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand:
    ''' Рука: набор карт на руках у одного игрока. '''
    
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        if self.cards:
           rep = ''
           for card in self.cards:
               rep += str(card) + '\t'
        else:
            rep = '<пусто>'
        return rep

    def clear(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Не могу больше сдавать: карты закончились!')
deck1 = Deck()
deck1.populate()
deck1.shuffle()
hands = []
u = 1

for i in range(0, int(input('Кол-во игроков'))):
    if i < 6:
        hand = Hand()
        hands.append(hand)
    else:
        print('Максимум 6 игроков. Раздаю только на 6')
        break

deck1.deal(hands, per_hand = 6)
for i in hands:
    print('\nКарты ', u, 'Игрока')
    print(i)
    u += 1