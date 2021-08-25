import copy
import os
from time import sleep
from square import AllSquares
from models import chess_piece_models
from chess_pieces import ChessPieces
from piece import Pawn, Knight, Bishop, Rook, Queen, King

__piece_class_list__ = [Pawn, Knight, Bishop, Rook, Queen, King]


class ChessBoard:
    def __init__(self):
        self.squares = AllSquares()
        self.all_chess_piece = ChessPieces(__piece_class_list__, chess_piece_models)
        self.__all_move_list__ = []
        self.is_pieces_moved = False

    def __parse_san__(self, san):
        pass

    def update_move(self, san):
        self.__all_move_list__.append(san)
        from_square = san[0]+san[1]
        to_square = san[2]+san[3]
        the_chess_piece_square = getattr(self.squares, from_square)
        the_chess_piece_square.chess_piece.current_position = to_square
        setattr(self.squares, to_square, the_chess_piece_square)
        setattr(self.squares, from_square, "\uFF3F")

    def get_all_moves(self):
        return self.__all_move_list__

    def __visualize_chess_board__(self, rank):
        for x in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print("|", getattr(self.squares, str(x) + str(rank)), end=" ")
        print(f"| {rank} \n")

    # The screen clear function
    def screen_clear(self):
        pass

    def visualize_chess_board(self):
        self.screen_clear()
        rank = 8
        while rank >= 1:
            self.__visualize_chess_board__(rank)
            rank = rank - 1

    def load_black_pawn(self, pawn_object):
        white_pawn_default_square = {'a7': copy.deepcopy(pawn_object), 'b7': copy.deepcopy(pawn_object),
                                     'c7': copy.deepcopy(pawn_object), 'd7': copy.deepcopy(pawn_object),
                                     'e7': copy.deepcopy(pawn_object), 'f7': copy.deepcopy(pawn_object),
                                     'g7': copy.deepcopy(pawn_object), 'h7': copy.deepcopy(pawn_object)}

        for square in white_pawn_default_square:
            if hasattr(self.squares, square):
                load_piece_at = getattr(self.squares, square)
                load_piece_at.chess_piece = white_pawn_default_square[square]

    def load_black_pieces(self, all_black_pieces):
        black_piece_default_square = {'a8': all_black_pieces['Rook'], 'b8': all_black_pieces['Knight'],
                                      'c8': all_black_pieces['Bishop'], 'd8': all_black_pieces['Queen'],
                                      'e8': all_black_pieces['King'], 'f8': copy.deepcopy(all_black_pieces['Bishop']),
                                      'g8': copy.deepcopy(all_black_pieces['Knight']),
                                      'h8': copy.deepcopy(all_black_pieces['Rook'])}

        for square in black_piece_default_square:
            if hasattr(self.squares, square):
                load_piece_at = getattr(self.squares, square)
                load_piece_at.chess_piece = black_piece_default_square[square]
        self.load_black_pawn(all_black_pieces['Pawn'])

    def load_white_pawn(self, pawn_object):
        white_pawn_default_square = {'a2': copy.deepcopy(pawn_object), 'b2': copy.deepcopy(pawn_object),
                                     'c2': copy.deepcopy(pawn_object), 'd2': copy.deepcopy(pawn_object),
                                     'e2': copy.deepcopy(pawn_object), 'f2': copy.deepcopy(pawn_object),
                                     'g2': copy.deepcopy(pawn_object), 'h2': copy.deepcopy(pawn_object)}

        for square in white_pawn_default_square:
            if hasattr(self.squares, square):
                load_piece_at = getattr(self.squares, square)
                load_piece_at.chess_piece = white_pawn_default_square[square]

    def load_white_pieces(self, all_white_pieces):
        white_piece_default_square = {'a1': all_white_pieces['Rook'], 'b1': all_white_pieces['Knight'],
                                      'c1': all_white_pieces['Bishop'], 'd1': all_white_pieces['Queen'],
                                      'e1': all_white_pieces['King'], 'f1': copy.deepcopy(all_white_pieces['Bishop']),
                                      'g1': copy.deepcopy(all_white_pieces['Knight']),
                                      'h1': copy.deepcopy(all_white_pieces['Rook'])}

        for square in white_piece_default_square:
            if hasattr(self.squares, square):
                load_piece_at = getattr(self.squares, square)
                load_piece_at.chess_piece = white_piece_default_square[square]
        self.load_white_pawn(all_white_pieces['Pawn'])

    def load_pieces(self):
        all_pieces = self.all_chess_piece.build_chess_pieces()
        self.load_black_pieces(all_pieces['black'])
        self.load_white_pieces(all_pieces['white'])






