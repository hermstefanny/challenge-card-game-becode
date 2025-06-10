from typing import List
from random import shuffle, choice
from utils.card import Card


class Player:
    """Class Player definition"""

    def __init__(
        self,
        name: str,
        cards: List[Card],
        turn_count: int,
        number_of_cards: int,
        history: List[Card],
    ) -> None:
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def __str__(self) -> str:
        """Returns string defining attributes from Player"""

        return f"{self.name} has the following cards: {self.cards}, their history of cards is {self.history}"

    def play(self) -> Card | None:
        """Player picks randomly a card from their stack"""
        if not self.cards:
            return None

        selected_card = choice(self.cards)
        self.history.append(selected_card)
        print(f"{self.name} in its {self.turn_count} turn played: {selected_card}")
        self.cards.remove(selected_card)

        return selected_card

    def display_players_cards(self) -> None:
        print(f"\n{self.name} has the following cards:")
        print(len(self.cards))
        for card in self.cards:
            print(card)


class Deck:
    """Class Deck definition"""

    def __init__(self) -> None:
        self.deck_cards = []

    def __str__(self) -> str:
        """This function will display each card with its corresponding value, symbol and color"""
        """Returns a string with the numbers of cards in the deck"""

        for card in self.deck_cards:
            print(f"This unique card is {card}")

        return f"Number of cards in this desk: {len(self.deck_cards)}"

    def fill_deck(self) -> None:
        """Function to create all 52 cards, assigning an icon, a color and a value"""
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
                self.deck_cards.append(card)

    def shuffle(self) -> None:
        """Function to randoming shuffle the deck of cards"""
        shuffle(self.deck_cards)

    def distribute(self, players: List[Player]) -> List[Player]:
        """Distributes the cards on deck one at the time, one player at the time"""

        n_cards = len(self.deck_cards) // len(players)
        print(n_cards)

        for i, player in enumerate(players):
            cards_for_player = self.deck_cards[0:n_cards]
            player.cards.extend(cards_for_player)
            for card in cards_for_player:
                self.deck_cards.remove(card)
