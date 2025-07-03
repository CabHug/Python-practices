#CHallenge to develop a game

# In this game you will have a destructor (D), battleship (B) and submarine (S) each one will have a specific position in your field game,
# In each try you will gave a position and wait for a result

class Game_Field:
    def __init__(self, p, d=5):
        self.d = d # Dimention of filed
        self.p = p # Pattern of field
        self.game = [[self.p for i in range(0,self.d)] for i in range(0,self.d)] 
        self.nave = {
            'D': 2,
            'B': 3,
            'S': 4
        }
    
    def get_fiel(self):
        for fila in self.game:
            print(" ".join(f"{elem:>3}" for elem in fila))


class Player:
    def __init__(self, field):
        self.field = field
        self.naves = {}

    # Return True if in this position already exist any ship
    def Check_point(self, x, y, fld=None):
        c_field = fld if fld is not None else self.field
        check = ['D','B','S']
        for i in check:
            if c_field.game[x][y] == i:
                return [True, i]
        return [False, i]
            
    # Return True if this point can be in the field
    def Check_size(self, x, y, fld=None):
        c_field = fld if fld is not None else self.field
        d = c_field.d
        if (x >= 0 and x < d) and (y >= 0 and y < d):
            return True
        else:
            return False

    # Set nave inside game field
    def Set_nave(self, x, y, type, rotation):
        lengh = self.field.nave[type]
        points =[]
        for p in range(0,lengh):
            xp = x+p
            if rotation != 0:
                yp = y+(p*rotation)
            else:
                yp = y
            if self.Check_size(xp, yp) and not self.Check_point(xp, yp)[0]:
                points.append([xp,yp])
            else:
                print(f"ERROR! Please try another coodinates! for {type}")
                return
        self.naves[type] = points
        for c in points:
            self.field.game[c[0]][c[1]] = type

    def Shoot(self, x, y, player):
        if self.Check_size(x, y, player.field):
            if self.Check_point(x, y, player.field)[0]:
                coor = player.naves[self.Check_point(x, y, player.field)[1]]
                for c in coor:
                    player.field.game[c[0]][c[1]] = 'X'
                print(f"You have sunk de ship! :c")
            else:
                player.field.game[x][y] = 'x'
                print("You have shot! ")
        else:
            print("Shoot out of range, try again! :V")



player1 = Game_Field('*', 10)
#player1.get_fiel()

player2 = Game_Field('-', 10)
#player2.get_fiel()

# Field configuration
Hugo = Player(player1)
Hugo.Set_nave(3,3,'D',-1)
Hugo.Set_nave(4,9,'B',-1)


Andres = Player(player2)
Andres.Set_nave(4,3,'D',1)
Andres.Set_nave(6,6,'S',0)

# status
player1.get_fiel()
player2.get_fiel()

Hugo.Shoot(6,6, Andres)
Hugo.Shoot(3,6, Andres)

# status
player1.get_fiel()
player2.get_fiel()

Andres.Shoot(3,4, Hugo)
Andres.Shoot(3,3, Hugo)

# status
player1.get_fiel()
player2.get_fiel()



