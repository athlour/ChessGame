'''

This class is an interface for all Chess Piece class (Pawn, Knight, Bishop, Rook, Queen, King)

'''


class ChessPieces:
    def __init__(self, list_chess_piece_class, model):
        self.class_list = list_chess_piece_class
        self.model = model

    def __build_chess_object__(self, class_name, chess_piece_data_model):
        chess_piece_object = class_name(chess_piece_data_model["chess_piece_name"],
                                        chess_piece_data_model["chess_piece_color"],
                                        chess_piece_data_model["chess_piece_symbol"],
                                        chess_piece_data_model["chess_piece_unicode"],
                                        chess_piece_data_model["chess_piece_relative_value"],
                                        chess_piece_data_model["chess_piece_default_position"])
        return chess_piece_object

    def __build_chess_objects__(self, class_list, model_dict):
        list_chess_piece = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]
        chess_objects = {}
        index = 0
        for class_name in class_list:
            chess_object = self.__build_chess_object__(class_name, model_dict[list_chess_piece[index]])
            chess_objects.update({chess_object.name: chess_object})
            index = index + 1
        return chess_objects

    def build_chess_pieces(self):
        white = self.__build_chess_objects__(self.class_list, self.model["white"])
        black = self.__build_chess_objects__(self.class_list, self.model["black"])
        return {"white": white, "black": black}




