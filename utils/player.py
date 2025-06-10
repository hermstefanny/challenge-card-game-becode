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
        """Class Player constructor that assigns the class attributes"""
        self.name = name
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history

    def __str__(self) -> str:
        """String that defines the class Player"""

        return f"{self.name} has played a total of {self.turn_count} turns with these cards: {self.history}"

    def play(self) -> Card | None:
        """
        Player plays a card:
        1. If there are no cards, returns None
        2. Randomly selects a card from their stack
        3. Adds the card to the history of played cards
        4. Prints the move
        5. Removes the selected card from player deck of cards
        6. Returns the selected card
        """

        if not self.cards:
            return None

        selected_card = choice(self.cards)
        self.history.append(selected_card)
        print(f"{self.name} in its turn {self.turn_count} played: {selected_card}")
        self.cards.remove(selected_card)

        return selected_card

    def display_players_cards(self) -> None:
        """Displays cards in player deck (not history)"""

        print(f"\n{self.name} has {len(self.cards)} cards:")
        for card in self.cards:
            print(card)


class Deck:
    """Class Deck definition"""

    def __init__(self) -> None:
        """Class Deck constructor that initilizes the deck with empty list of cards"""

        self.deck_cards = []

    def __str__(self) -> str:
        """String that defines the Class Deck, by showing the number of cards"""

        return f"Number of cards in this deck: {len(self.deck_cards)}"

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
        """Random shuffle the deck of cards"""

        shuffle(self.deck_cards)

    def distribute(self, players: List[Player]) -> None:
        """
        Distributes the deck of cards one player at the time:
        It is going to distribute an equal number of cards to all players.
        If the number of cards is not perfectly divisible by the players, the remaining cards will stay in the deck
        1. Calculates the number of cards that every player will receive
        2. Creates a sublist with copies of the cards according to its numbers
        3. Adds this sublist to the player cards
        4. Removes this cards from the deck
        """

        n_cards = len(self.deck_cards) // len(players)

        for player in players:
            cards_for_player = self.deck_cards[0:n_cards]
            player.cards.extend(cards_for_player)

            for card in cards_for_player:
                self.deck_cards.remove(card)

    def display_deck(self) -> None:
        """Display the cards currently on deck in order"""

        for card in self.deck_cards:
            print(f"The card is {str(card)}")
