from utils.game import Board
from utils.game import Player

if __name__ == "__main__":

    player_1 = Player("Thomas", [], 0, 0, [])
    player_2 = Player("Rose", [], 0, 0, [])
    player_3 = Player("Joseph", [], 0, 0, [])
    # player_4 = Player("Diane", [], 0, 0, [])

    active_players = [player_1, player_2, player_3]

    board = Board(active_players, 0, [], [])
    board.start_game()
    # board.play_game()
