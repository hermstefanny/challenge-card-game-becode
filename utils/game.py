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
        deck = Deck()
        deck.fill_deck()
        print("-----------Before shuffling -----------------")
        print(deck)
        deck.shuffle()
        print("-----------AFTER shuffling -----------------")
        print(deck)

        player_1 = Player("Thomas", [], 0, 0, [])
        player_2 = Player("Rose", [], 0, 0, [])
        player_3 = Player("Joseph", [], 0, 0, [])
        player_4 = Player("Diane", [], 0, 0, [])

        active_players = [player_1, player_2, player_3, player_4]

        deck.distribute(active_players)

        for player in active_players:
            print(player.display_players_cards())

        print(deck)
