from piece import Bishop

chess_piece_name = 'Bishop'
chess_piece_color = 'White'
chess_piece_symbol = 'B'
chess_piece_unicode = '\u2657'
chess_piece_relative_value = 3
chess_piece_default_position = "c8"

bishop = Bishop(chess_piece_name, chess_piece_color, chess_piece_symbol, chess_piece_unicode,
               chess_piece_relative_value,chess_piece_default_position)
print(bishop)
print(bishop.get_next_possible_positions())