import random

raceLength = 200
horse1 = 0
horse2 = 0

while horse1<raceLength or horse2<raceLength:
    horse1 = horse1+random.randint(1,12) * 2
    horse2 = horse2+random.randint(1,12) * 2

if horse1 == horse2:
    print("Tie!")
elif horse1>horse2:
    print("Horse 1 WINS!")
else:
    print("Horse 2 WINS!")
