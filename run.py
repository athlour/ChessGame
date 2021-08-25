from stockfish import Stockfish

stockfish = Stockfish("C:\\Users\\Athlour\\PycharmProjects\\ChessGame\\infrastructure\\stockfish_13_win_x64\\stockfish_13_win_x64")
f=["e2e4"]
print(f[0])
stockfish.set_position(f)
print(stockfish.get_board_visual())
bestmove = stockfish.get_best_move()
print(bestmove)