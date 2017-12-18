from C_ListObject import ListObject


class CombatOption(ListObject):
    GRAPPLED = 1
    MENDING = 2
    MAIMED = 3
    CRIPPLED = 4
    WOUNDED = 5

    def __init__(self,name, range, attack, defense, speedMod = 0, delayMod =0, damageMod = 0,freeMove = False,forwardMove = False, awayMove = False, push = False, pull = False, statusesAdded = [WOUNDED], statusesRemoved = []):
        global DEFAULT_ATTACKS
        self.attackMod = attack
        self.range = range
        self.name = name
        self.defenseMod = defense
        self.damageMod = damageMod
        self.speedMod = speedMod
        self.delayMod = delayMod
        self.freeMove = freeMove
        self.forwardMove = forwardMove
        self.awayMove = awayMove
        self.statusesAdded = statusesAdded
        self.statusesRemoved = statusesRemoved
        DEFAULT_ATTACKS.append(self)
def createBasicOptions():
    CombatOption("Push",-2,1,1,0,0,0,False,False,False,True)
    CombatOption("Backstep",-2,-5,-3,0,0,0,False,False,True)
    CombatOption("Back Attack",-1,1,-2,0,0,0,False,False,True)
    CombatOption("Backstep",-2,-2,0,0,0,False,False,True)
    CombatOption("Power Attack",0,3,0,0,-3,3)
    CombatOption("Guard",0,0,8,0,0,0)
    CombatOption("Forward Attack",1,1,-2,0,0,0,False,True,False)
    CombatOption("Guarded Approach",1,-2,-2,0,0,0,False,True,False)
    CombatOption("Jumping Swing",2,1,-5,0,0,0,False,True,False)
    CombatOption("Forward Run",2,-5,-3,0,0,0,False,True,False)

DEFAULT_ATTACKS = []

createBasicOptions()

