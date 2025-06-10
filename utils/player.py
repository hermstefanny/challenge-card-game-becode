from typing import List
from utils.card import Card


class Player:
    """Class Player definition"""

    def __init__(
        self,
        cards: List[Card],
        turn_count: int,
        number_of_cards: int,
        history: List[Card],
    ) -> None:
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def play(self) -> Card:
        pass


class Deck:
    """Class Deck definition"""

    def __init__(self) -> None:
        self.cards = []

    def fill_deck(self) -> None:
        for icon in ["♥", "♦", "♣", "♠"]:
            if icon in ["♥", "♦"]:
                color = "red"
            else:
                color = "black"

            for value in [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ]:
                card = Card(color, icon, value)
                self.cards.append(card)

    def shuffle(self) -> None:
        pass

    def distribute(self, players: List[Player]) -> List[Player]:
        pass

    # To display the cards
    def display_deck(self) -> None:
        for card in self.cards:
            print(f"This unique card is {card}")

        print(f"The number of cards is {len(self.cards)}")
