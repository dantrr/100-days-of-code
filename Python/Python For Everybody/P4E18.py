class PartyAnimal:
    x=0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
###
#bam, that's a class.
###
class DestroyBuildDestroy:
    y=0
    def __init__(self):
        print("I'm born!")
    
    def count(self):
        self.y = self.y + 1
        print("Counting..", self.y)
    
    def __del__(self):
        print("I'M BEING DELETED!", self.y)

pow = DestroyBuildDestroy()
pow.count()
pow.count()
pow=42
print(f"pow is now {pow}")

class NameCaller:
    n=0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    
    def namey(self):
        self.n = self.n + 1
        print(f"{self.name} hosted {self.n} parties.")

b = NameCaller("Billy Bob")
b.namey()

a = NameCaller("Ashlee")
a.namey()
b.namey()

#object inheritance

# a subclass can "inherit" capabilities of a class, and extend it into a new class

class footballScore(NameCaller):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.namey
        print(f"{self.name} earned {self.points} points!")

f = footballScore("Frank West")
f.touchdown()