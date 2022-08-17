life0 = 20
life1 = 20
commanderLife0 = 40
commanderLife1 = 40
commanderLife2 = 40
commanderLife3 = 40
commanderLife4 = 40
commanderLife5 = 40
commanderLife6 = 40
commanderLife7 = 40
brawlLife0 = 25
brawlLife1 = 25
poisonCount0 = 0
poisonCount1 = 0
poisonCount2 = 0
poisonCount3 = 0
poisonCount4 = 0
poisonCount5 = 0
poisonCount6 = 0
poisonCount7 = 0
commanderDmg0 = 0
commanderDmg1 = 0
commanderDmg2 = 0
commanderDmg3 = 0
commanderDmg4 = 0
commanderDmg5 = 0
commanderDmg6 = 0
commanderDmg7 = 0

def p0hit(x):
    life0-x
    print(f"Player 1 has {life0} remaining.")

def p1hit(x):
    life1-x
    print(f"Player 2 has {life1} remaining.")

while life0 or life1 > 0:
    #placeholder


p0hit(10)