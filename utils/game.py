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
        deck.display_deck()
