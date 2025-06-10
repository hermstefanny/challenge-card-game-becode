from typing import List
from card import Card


class Player:
    """Class Player definition"""

    def __init__(
        self, card: Card, turn_count: int, number_of_cards: int, history: List[Card]
    ) -> None:
        self.card = card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def play(self) -> Card:
        pass


class Deck:
    """Class Deck definition"""

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def fill_deck(self) -> None:
        pass

    def shuffle(self) -> None:
        pass

    def distribute(self, players: List[Player]) -> List[Player]:
        pass
