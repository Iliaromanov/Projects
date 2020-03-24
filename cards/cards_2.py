# A class for creating and organizing playing cards
class PlayingCard:
    full_deck = []
    hearts = []
    diamonds = []
    spades = []
    clubs = []

    def __init__(self, card_value: int, suite: str):
        self.card_value = card_value
        self.suite = suite
        PlayingCard.full_deck.append(self)

    def __str__(self) -> str:
        return f"{self.card_value}, {self.suite}"
    
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
