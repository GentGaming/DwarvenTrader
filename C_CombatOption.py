from C_ListObject import ListObject

class CombatOption(ListObject):
    GRAPPLED = 1
    MENDING = 2
    MAIMED = 3
    CRIPPLED = 4
    WOUNDED = 5

    def __init__(self,name, attack,defense,damageMod,freeMove = False,forwardMove = False, awayMove = False,statusesAdded = [], statusesRemoved = []):
        self.attackMod = attack
        self.defenseMod = defense
        self.damageMod = damageMod
        self.freeMove = freeMove
        self.forwardMove = forwardMove
        self.awayMove = awayMove
        self.statusesAdded = statusesAdded
        self.statusesRemoved = statusesRemoved


LUNGE = CombatOption("Lunge",0,-2,1,False,True,False)
PARRY = CombatOption("Parry",-4,2,-3,True,False,False)
ATTACK = CombatOption("Attack",1,1,0,False,False,False)
FEINT = CombatOption("Feint",-8,-8,0,False,True,False)

# and more later...
