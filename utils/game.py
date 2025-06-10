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
    ):
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

    def start_game(self):
        """
        Function that plays the game:
        1. Creating the deck and filling it with cards
        2. Shuffling the cards deck
        3. Distributing the cards to the players
        4. Starting the play by delivering the cards
        """

        deck = Deck()
        deck.fill_deck()
        print("-----------Before shuffling -----------------")
        print(deck)
        deck.shuffle()
        print("-----------AFTER shuffling -----------------")
        print(deck)

        deck.distribute(self.players)

        for player in self.players:
            player.display_players_cards()
            print("-----Cards distributed----")

    def play_game(self) -> None:

        player_finished = [False for player in self.players]

        while not all(player_finished):
            for i, player in enumerate(self.players):
                if player.cards:
                    player.turn_count += 1
                    card_played = player.play()

                else:
                    player_finished[i] = True

        print("All players have dealt their cards")
