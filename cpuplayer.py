from stockfish import Stockfish

class CPUPlayer():
    def __init__(self, arbiter_object):
        self.arbiter = arbiter_object
        print(self.arbiter)
        self.moves = []

    def __get_move__(self):
        stockfish = Stockfish("C:\\Users\\Athlour\\PycharmProjects\\ChessGame\\infrastructure\\stockfish_13_win_x64\\stockfish_13_win_x64")
        move = self.arbiter.chessboard.get_all_moves()
        stockfish.set_position(move)
        my_move = stockfish.get_best_move()
        print(my_move)
        return my_move

    def set_move(self):
        self.arbiter.update_move(self.__get_move__())
