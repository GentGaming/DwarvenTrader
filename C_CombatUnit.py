from C_Actor import Actor
import C_CombatOption
class CombatUnit(Actor):
    def __init__(self,name,strength,agi,con):
        super().__init__()
        self.strength = strength
        self.agility = agi
        self.constitution = con
        self.xPos = 0
        self.yPos = 0
        self.equippedWeapon = None
        self.meleeOptions = C_CombatOption.DEFAULT_ATTACKS
        self.currentStatuses = []
    def getCombatOptionsRelativeToEnemy(self,enemy):
        dx = abs(self.xPos - enemy.xPos)
        dy = abs(self.yPos - enemy.yPos)
        d = min(dx,dy)
        effectiveRange = d - self.weapon.range
        ret = []
        for o in self.meleeOptions:
            if o.range == effectiveRange:
                ret.append(o)
        return ret
    def addStatus(self,status):
        if not self.currentStatuses.__contains__(status):
            self.currentStatuses.append(status)
    def removeStatus(self,status):
        self.currentStatuses.remove(status)
