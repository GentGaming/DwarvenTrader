from C_ListObject import ListObject

class CombatOption(ListObject):
    GRAPPLED = 1
    MENDING = 2
    MAIMED = 3
    CRIPPLED = 4
    WOUNDED = 5

    def __init__(self,name, attack, defense, speedMod = 0, delayMod =0, damageMod = 0,freeMove = False,forwardMove = False, awayMove = False, push = False, pull = False, statusesAdded = [], statusesRemoved = []):
        self.attackMod = attack
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


#-2 only self polearm v  opponent grapple
PUSH = CombatOption("Push",1,1,0,0,0,False,False,False,True)
BACKRUN = CombatOption("Backstep",-5,-3,0,0,0,False,False,True)
#-1
BACKATTACK = ("BackAttack",1,-2,0,0,0,False,False,True)
BACKSTEP = CombatOption("Backstep",-2,-2,0,0,0,False,False,True)
#0
POWERATTACK = CombatOption("PowerAttack",3,0,0,-3,3)
GUARD = CombatOption("Guard",0,8,0,0,0)
#1
BACKATTACK = ("ForwardAttack",1,-2,0,0,0,False,True,False)
GUARDEDAPPROACH = ("GuardedApproach",-2,-2,0,0,0,False,True,False)
#2
JUMPINGSWING = ("JumpingSwing",1,-5,0,0,0,False,True,False)
RUNFORWARDS = ("ForwardRun",-5,-3,0,0,0,False,True,False)
#3
#empty because if only lives with three range weapons..

LUNGE = CombatOption("Lunge",0,-2,1,False,True,False)
PARRY = CombatOption("Parry",-4,2,-3,True,False,False)
ATTACK = CombatOption("Attack",1,1,0,False,False,False)
FEINT = CombatOption("Feint",-8,-8,0,False,True,False)

# and more later...
