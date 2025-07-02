#CHallenge to develop a game

# In this game you will have a destructor (D), battleship (B) and submarine (S) each one will have a specific position in your field game,
# In each try you will gave a position and wait for a result

class Game_Field:
    def __init__(self, p, d=10):
        self.d = d
        self.p = p
        self.game = [[self.p for i in range(0,self.d)] for i in range(0,self.d)]

field1 = Game_Field('*')
print(field1.game)

field2 = Game_Field('-')
print(field2.game)

field2.game[0][0] = 'o'

print(field2.game)

"""
class Player:
    def __init__(self, field):
        self.field = field

    def Check(self, x, y):
        if self.field[x][y]

    #size 2
    def Set_Destuctor(self, x, y):
         d = len(self.field)
         if (x >= 0 and x < d) and (y >= 0 and y < d):
"""