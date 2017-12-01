import random

class Combat:
    def __init__(self,combatants):
        self.combatants = combatants
    def establishInitiative(self):
        goodguyinitiative = 1
        badguyinitiative = 2
        initiativelist = [goodguyinitiative,badguyinitiative]
        return initiativelist
    def updateCombat(self):
        health=health-damage
        return health
    def calculateDamage(self):
        i=0
        damage=0
        while i < 3:
            damage+=random.randint(1,6)
        print(damage)
        return damage
    def autoCombat(self):
        while health < 15%:
            flee
        else attack
