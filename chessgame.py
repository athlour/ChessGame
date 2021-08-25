from humanplayer import HumanPlayer
from cpuplayer import CPUPlayer
from arbiter import Arbiter


class ChessGame:
    def __init__(self):
        self.arbiter = Arbiter()
        self.Human_player = HumanPlayer(self.arbiter)
        self.CPU_Player = CPUPlayer(self.arbiter)

    def human_player_play(self):
        player_move = input("Enter the Move (e.x : e2e4) : ")
        self.Human_player.set_move(player_move)

    def cpu_player_play(self):
        self.CPU_Player.set_move()

    def play(self):
        while True:
            self.arbiter.chessboard.visualize_chess_board()
            self.human_player_play()
            self.cpu_player_play()


if __name__ == "__main__":
    game = ChessGame()
    game.play()


