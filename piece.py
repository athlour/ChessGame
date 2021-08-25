from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, chess_piece_name, chess_piece_color, chess_piece_symbol,
                 chess_piece_unicode, chess_piece_relative_value, chess_piece_default_position):
        self.name = chess_piece_name
        self.color = chess_piece_color
        self.piece_symbol = chess_piece_symbol
        self.piece_unicode = chess_piece_unicode
        self.relative_value = chess_piece_relative_value
        self.default_position = chess_piece_default_position
        self.current_position = None
        self.Next_Possible_Positions = []

    @abstractmethod
    def get_next_possible_positions(self):
        pass

    def __repr__(self):
        if self.piece_unicode == None:
            return self.piece_symbol
        else:
            return self.piece_unicode


class Pawn(Piece):
    def get_next_possible_positions(self):
        pass

"""
A knight moves on an extended diagonal from one corner of any two-by-three rectangle of squares to the farthest 
opposite corner. Consequently, the knight alternates its square color each time it moves.Other than the castling move 
described above where the rook jumps over the king, the knight is the only piece permitted to routinely jump over any
intervening piece(s) when moving.
"""


class Knight(Piece):
    def __possible_horizontal_directions__(self, current_square_coordinates):
        list_of_possible_horizontal_directions = []
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        no_of_vertical_steps = 1
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_index = None
        # find one right and left rank
        for rank_index in range(1, 8):
            if current_rank == ranks[rank_index]:
                current_index = rank_index
        if current_file == "1":
            list_of_possible_horizontal_directions = [ ]
        else:
            possible_up_left_direction = ranks[current_index - 2] + str(int(current_file) + int(no_of_vertical_steps))
            possible_up_right_direction = ranks[current_index + 2] + str(int(current_file) + int(no_of_vertical_steps))
            possible_down_left_direction = ranks[current_index - 2] + str(int(current_file) - int(no_of_vertical_steps))
            possible_down_right_direction = ranks[current_index + 2] + str(
                int(current_file) - int(no_of_vertical_steps))
            list_of_possible_horizontal_directions = [possible_up_left_direction, possible_up_right_direction,
                                                      possible_down_left_direction, possible_down_right_direction]
        return list_of_possible_horizontal_directions

    def __possible_vertical_directions__(self, current_square_coordinates):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        no_of_vertical_steps = 2
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_index = None
        # find one right and left rank
        for rank_index in range(1, 8):
            if current_rank == ranks[rank_index]:
                current_index = rank_index
        if current_file == "1":
            possible_up_left_direction = ranks[current_index - 1] + str(int(current_file) + int(no_of_vertical_steps))
            possible_up_right_direction = ranks[current_index+1] + str(int(current_file) + int(no_of_vertical_steps))
            list_possible_vertical_directions = [possible_up_left_direction, possible_up_right_direction]
        else:
            possible_up_left_direction = ranks[current_index - 1] + str(int(current_file) + int(no_of_vertical_steps))
            possible_up_right_direction = ranks[current_index + 1] + str(int(current_file) + int(no_of_vertical_steps))
            possible_down_left_direction = ranks[current_index - 1] + str(int(current_file) - int(no_of_vertical_steps))
            possible_down_right_direction = ranks[current_index + 1] + str(int(current_file) - int(no_of_vertical_steps))
            list_possible_vertical_directions = [possible_up_left_direction, possible_up_right_direction,
                                                 possible_down_left_direction, possible_down_right_direction]
        return list_possible_vertical_directions

    """ moving two squares horizontally then one square vertically, 
    or moving one square horizontally then two squares vertically—i.e. in an "L" pattern """
    def get_next_possible_positions(self):
        current_square_coordinates = []
        try:
            for char in self.current_position:
                current_square_coordinates.append(char)
        except Exception as e:
            for char in self.default_position:
                current_square_coordinates.append(char)

        vertical_directions = self.__possible_vertical_directions__(current_square_coordinates)
        horizontal_directions = self.__possible_horizontal_directions__(current_square_coordinates)
        list_next_possible_positions = vertical_directions + horizontal_directions
        self.Next_Possible_Positions = list_next_possible_positions
        return list_next_possible_positions


"""
A bishop moves any number of vacant squares diagonally in a straight line. Consequently, a bishop stays on squares of 
the same color throughout a game. The two bishops each player starts with move on squares of opposite colors. 
Move denoted by "X"
"""


class Bishop(Piece):
    # https://www.geeksforgeeks.org/count-the-total-number-of-squares-that-can-be-visited-by-bishop-in-one-move/
    # Python3 implementation of above approach
    # Function to return the count of
    # total positions the Bishop
    # can visit in a single move
    def countsquares(self, row, column):
        top_left = min(row, column) - 1
        top_right = min(row, 9 - column) - 1
        bottom_right = 8 - max(row, column)
        bottom_left = 8 - max(row, 9 - column)
        return (top_left,  top_right, bottom_right, bottom_left)

    def __possible_top_left_diagonal_directions__(self, current_square_coordinates):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_rank_index = ranks.index(current_rank)
        top_left = min(current_rank_index + 1, 9 - int(current_file)) - 1
        print('top left', top_left)


    def __possible_top_right_diagonal_directions__(self, current_square_coordinates):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_rank_index = ranks.index(current_rank)
        top_right = 8 - max(current_rank_index + 1, int(current_file))
        print('top right', top_right)



    def __possible_bottom_right_diagonal_directions__(self, current_square_coordinates):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_rank_index = ranks.index(current_rank)
        bottom_right =  min(current_rank_index +1 , int(current_file)) - 1
        print('bottom_right', bottom_right)


    def __possible_bottom_left_diagonal_directions__(self, current_square_coordinates):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        current_rank = current_square_coordinates[0]
        current_file = current_square_coordinates[1]
        current_rank_index = ranks.index(current_rank)
        bottom_left = 8 - max(current_rank_index + 1, 9 - int(current_file))
        print('bottom_left', bottom_left)



    def get_next_possible_positions(self):
        current_square_coordinates = []
        moves = []
        try:
            for char in self.current_position:
                current_square_coordinates.append(char)
        except Exception as e:
            for char in self.default_position:
                current_square_coordinates.append(char)

        top_left = self.__possible_top_left_diagonal_directions__(current_square_coordinates)
        top_right = self.__possible_top_right_diagonal_directions__(current_square_coordinates)
        bottom_left = self.__possible_bottom_left_diagonal_directions__(current_square_coordinates)
        bottom_right = self.__possible_bottom_right_diagonal_directions__(current_square_coordinates)
        # print('top_left',top_left)
        # print('top_right', top_right)
        # print('bottom_left', bottom_left)
        # print('bottom_right', bottom_right)




"""
A rook moves any number of vacant squares forwards, backwards, left, or right in a straight line.
It also takes part, along with the king, in a special move called castling. Move denoted by "+"
"""


class Rook(Piece):
    def __possible_horizontal_directions__(self, current_square_coordinates):
        list_of_possible_horizontal_directions = []
        return list_of_possible_horizontal_directions

    def __possible_vertical_directions__(self, current_square_coordinates):
        list_possible_vertical_directions = []
        return list_possible_vertical_directions

    def get_next_possible_positions(self):
        pass



"""
The queen moves any number of vacant squares in any direction: forwards, backwards, left, right, or diagonally,
in a straight line.
"""


class Queen(Piece):
    def __possible_horizontal_directions__(self, current_square_coordinates):
        list_of_possible_horizontal_directions = []
        return list_of_possible_horizontal_directions

    def __possible_vertical_directions__(self, current_square_coordinates):
        list_possible_vertical_directions = []
        return list_possible_vertical_directions

    def get_next_possible_positions(self):
        pass


"""
The king moves exactly one vacant square in any direction: forwards, backwards, left, right, or diagonally; however, 
it cannot move to a square that is under attack by an opponent, nor can a player make a move with another piece if it 
will leave the king in check. It also has a special move called castling, in which the king moves two squares towards 
one of its own rooks and in the same move,the rook jumps over the king to land on the square on the king's other side. 
Castling may only be performed if the king and rook involved have never previously been moved in the game, 
if the king is not in check, if the king would not travel through or into check, and if there are no pieces 
between the rook and the king. 
"""


class King(Piece):
    def get_next_possible_positions(self):
        pass