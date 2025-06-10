from utils.game import Board
from utils.game import Player

if __name__ == "__main__":

    players_names = ["Thomas", "Rose", "Joseph", "Gerardo"]
    active_players = []

    for player_name in players_names:
        active_players.append(Player(player_name, [], 0, 0, []))

    board = Board(active_players, 0, [], [])
    board.start_game()
    # board.play_game()
