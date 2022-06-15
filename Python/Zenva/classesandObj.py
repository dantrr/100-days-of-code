# class is like the blueprint for an object, 
# and can represent a 
# game character for example, 
# with different attributes and variables such as health, items, etc. 

# classes have to be implemented before objects. 

class gameChar:
    def __init__(self, name, pos, health):
        self.name = name
        self.pos = pos
        self.health = health

    def move(self, by_amount):
        self.pos += by_amount

mainChar = gameChar("Clyde", 5, 400)