import re
from chessboard import ChessBoard


'''
Every chess tournament has at least one arbiter / tournament director to manage the play, rule on disputes,
and ensure a successful event.

an arbiter has four main responsibilities:
    1.Ensure that laws of chess (rules) are followed
    2.Prevent cheating
    3.Act in the “best interest of the competition”
    4.Observe the individual games

'''


class Arbiter:
    '''
    create rules model here
    '''
    def __init__(self):
        self.chessboard = ChessBoard()
        self.chessboard.squares.build_squares()
        self.chessboard.load_pieces()

    def checkmate(self):
        pass

    def check(self):
        pass

    def is_check(self):
        if self.check():
            if self.is_checkmate():
                return 'Who Win'



    def is_move_legal(self, san):
        from_square = san[0] + san[1]
        to_square = san[2] + san[3]
        the_chess_piece_from_square = getattr(self.chessboard.squares, from_square)
        the_chess_piece_to_square = getattr(self.chessboard.squares, to_square)
        try:
            possible_positions = the_chess_piece_from_square.chess_piece.get_next_possible_positions()
            print(possible_positions)
            for possible_position in possible_positions:
                if to_square == possible_position:
                    if isinstance(the_chess_piece_to_square.chess_piece, str):
                        return True
                    else:
                        print(the_chess_piece_to_square.chess_piece.color, the_chess_piece_from_square.chess_piece.color)
        except AttributeError:
            return False
        except TypeError:
            return False


    def is_valid_move(self, san):
        '''
        pattern = "[a-h][1-8]x[a-h][1-8][=][QRBN]|[a-h][1-8][=][QRBN]|" \
                  "[a-h][1-8][+#]|[EBRQNK][a-h][1-8][+#]|[EBRQNK][a-h][1-8]|[EBRQNK][a-h]x[a-h][1-8]" \
                  "|[EBRQNK][a-h][1-8]x[a-h][1-8]|[EBRQNK][a-h][1-8][a-h][1-8]|[EBRQNK][a-h][a-h][1-8]" \
                  "|[EBRQNK]x[a-h][1-8][++]|[EBRQNK]x[a-h][1-8]|[a-h]x[a-h][1-8]=(B+R+Q+N)" \
                  "|[a-h]x[a-h][1-8]|[a-h][1-8]x[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]x[a-h][1-8]|" \
                  "[a-h][1-8][a-h][1-8]=(B+R+Q+N)|[a-h][1-8][a-h][1-8]|[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]|" \
                  "[EBRQNK][1-8]x[a-h][1-8]"
        '''
        pattern = "[a-h][1-8][a-h][1-8]"
        regex = re.compile(pattern)
        if regex.match(san):
            if self.is_move_legal(san):
                return True
            else:
                return False
        else:
            return False

    def update_move(self, move):
        if self.is_valid_move(move):
            self.chessboard.update_move(move)
            # self.is_check()
            return True
        else:
            return False
