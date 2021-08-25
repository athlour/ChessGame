from dataclasses import dataclass


# Defining Squares class / object
@dataclass(repr=True)
class Square:
    UIN: str()
    square_color: str()
    chess_piece: None

    def __repr__(self):
        return str(self.chess_piece)


class AllSquares:
    def __init__(self):
        pass

    # Chess Board Model 8x8, total 64 squares, black 32 and white 32
    # The vertical columns of squares, called files
    # The horizontal rows of squares, called ranks
    #     \uFF3F ,
    def build_squares(self):
        ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
        colors = ["black", "white"]
        file = 1
        color_no = 0
        for x in range(64):
            for rank in ranks:
                square_object = Square(rank + str(file), colors[color_no], "\uFF3F")
                setattr(self, rank + str(file), square_object)
                color_no = color_no + 1
                if color_no == 2:
                    color_no = 0
            file = file + 1
            if file == 9:
                file = 1
        return None

