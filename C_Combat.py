import random

class Combat:
    def __init__(self,combatants):
        self.combatants = combatants
    def establishInitiative(self):
        goodguyinitiative = 1
        badguyinitiative = 2
        #incomplete
        initiativelist = [goodguyinitiative,badguyinitiative]
        return initiativelist
    def updateCombat(self):
        pass
        #health=health-damage
        #removed above correct code would be health -= damage if health and damage were defined.
        #return health
        #should not be called update combat and just change health.
    def calculateDamage(self):
        #this should live in CombatUnit
        '''
        i=0
        damage=0
        while i < 3:
            damage+=random.randint(1,6)
        print(damage)
        return damage
        '''
    def autoCombat(self):
        '''
        the % does not work like this.
        while health < 15%:

            flee
        '''