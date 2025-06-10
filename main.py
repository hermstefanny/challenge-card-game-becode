from utils.game import Board
from utils.game import Player

if __name__ == "__main__":
    """Main function where the game is played:
    1. Initiliazes the players list with their names and intial values
    2. Creates a board object by passing the"""

    players_names = ["Thomas", "Rose", "Joseph", "Gerardo"]
    active_players = []

    for player_name in players_names:
        active_players.append(Player(player_name, [], 0, 0, []))

    board = Board(active_players, 0, [], [])

    print("\n============STARTING GAME============")
    board.start_game()

    print("\n============PLAYING GAME============")
    board.play_game()
