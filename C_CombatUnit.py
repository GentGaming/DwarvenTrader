from C_Actor import Actor

class CombatUnit(Actor):
    def __init__(self,name,str,agi,con):
        super().__init__(name,str,agi,con)
        self.xPos = 0
        self.yPos = 0
        self.meleeOptionsByRange = [["a","b"], ["c","d"]]
    def getCombatOptionsRelativeToEnemy(self,enemy):
        dx = abs(self.xPos - enemy.xPos)
        dy = abs(self.yPos - enemy.yPos)
        d = min(dx,dy)

    def addStatus(self,status):
        #can only have one instance of a status
        pass
    def removeStatus(self,status):
        pass