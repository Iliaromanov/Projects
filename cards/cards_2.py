# A class for creating and organizing playing cards
class PlayingCard:
    full_deck = []
    hearts = {}
    diamonds = {}
    spades = {}
    clubs = {}

    def __init__(self, card_value: int, suite: str):
        self.card_value = card_value
        self.suite = suite
        PlayingCard.full_deck.append(self)

    def __str__(self) -> str:
        return f"{self.card_value}, {self.suite}"
    
    @staticmethod
    def make_cards():
        names = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

        i = 0

        while i < 13:
            PlayingCard.hearts[names[i]] = PlayingCard(i+1, 'hearts')
            
            i += 1

        j = 0

        while j < 13:
            PlayingCard.diamonds[names[j]] = PlayingCard(j+1, 'diamonds')
            
            j += 1

        k = 0

        while k < 13:
            PlayingCard.spades[names[k]] = PlayingCard(k+1, 'spades')
            
            k += 1

        l = 0

        while l < 13:
            PlayingCard.clubs[names[l]] = PlayingCard(l+1, 'clubs')
            
            l += 1

'''
    @staticmethod
    def sort():
        """Organizes cards into suites and assigns them color
        """
        for card in PlayingCard.full_deck:
            if card.suite == 'hearts':
                PlayingCard.hearts.append(card)
                card.color = 'red'
            elif card.suite == 'diamonds':
                PlayingCard.diamonds.append(card)
                card.color = 'red'
            elif card.suite == 'spades':
                PlayingCard.spades.append(card)
                card.color ='black'
            elif card.suite == 'clubs':
                PlayingCard.clubs.append(card)
                card.color = 'black'
'''


PlayingCard.make_cards()

print(len(PlayingCard.full_deck))
