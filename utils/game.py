from typing import List
from utils.player import Player, Deck
from utils.card import Card


class Board:
    def __init__(
        self,
        players: List[Player],
        turn_count: int,
        active_cards: List[Card],
        history_cards: List[Card],
    ) -> None:
        """Class Board constructor that assigns the class attributes"""
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

    def start_game(self):
        """
        Starts the game:
        1. Creates the object deck
        2. Fills it with cards
        3. Shuffles the cards deck
        4. Distributes the cards to the players
        5. Prints the initial configuration of the game
        """

        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)

        print("\n-----------Cards distributed-----------------")
        print("\nThe cards remaining on deck are:")
        print(deck)

    def play_game(self) -> None:
        """
        Plays the game:
        1. Establishes a list of flags that shows if each player has finished the game.
            1.1.Assigns <False> to all the players
        2. All flags must be <True> for the game to stop. Meanwhile:
            2.1.Loops along the list of players until all players:
                2.1.1. Prints the active cards in the turn
                2.1.2 If a player still has cards, add 1 to the counter of turns and call to the player's play function
                2.1.2. If a player does not have cards anymore, sets the corresponding flag to True
        3. Prints a final message
        """

        player_finished = [False for player in self.players]

        while not all(player_finished):

            for i, player in enumerate(self.players):
                if player.cards:

                    player.turn_count += 1
                    card_played = player.play()
                    print(f"The active cards in turn {player.turn_count} are:")
                    for card in self.active_cards:
                        print(card)

                    self.active_cards.append(card_played)
                    self.history_cards.append(card_played)

                else:
                    player_finished[i] = True
            self.active_cards = []

        print("Players have dealt all their cards")
