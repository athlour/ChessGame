class HumanPlayer:
    def __init__(self, arbiter_object):
        self.arbiter = arbiter_object
        print(self.arbiter)
        self.moves = []

    # display the board and and ask the player to move
    def set_move(self, move):
        self.moves.append(move)
        self.arbiter.update_move(move)

