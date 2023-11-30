class Piece:
    def __init__ (self, symbol, color):
        self.type = symbol
        self.color = color
    def __str__(self):
        if self.type == None:
            return " "
        return self.type
