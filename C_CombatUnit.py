from C_Actor import Actor

class CombatUnit(Actor):
    def __init__(self,name,str,agi,con,int):
        super().__init__(name,str,agi,con,int)
    def combat(self):
        #takes in 2 people, and gives options based on range from enemy and optimal range from enemy