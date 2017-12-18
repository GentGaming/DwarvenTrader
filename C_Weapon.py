from C_Equipment import Equipment
from C_CombatOption import CombatOption
class Weapon(Equipment):

    SWORD = 1
    AXE = 2
    HAMMER = 3
    BOW = 4
    X_BOW = 5

    SMALL = 6
    MEDIUM = 7
    LARGE = 8
    HUGE = 9

    def __init__(self,type,size,quality):
        self.createName()
        super().__init__()
        self.combatOptions = []
    def createName(self,type,size):
        s = CombatOption("The dagger in the ear attack", 0, -5, -3, 0, 0, 0, False, True, False)
        a = CombatOption("Arms race",0,-1,-2,1,0,0,False,False,False,False,False,[CombatOption.MAIMED])
        h = CombatOption("Break a leg", 0, 0, -1, 1, 0, 0, False, False, False, False, False, [CombatOption.CRIPPLED])
        g = CombatOption("liabilty risk", 0, 0, -1, 1, 0, 0, False, False, False, False, False, [CombatOption.CRIPPLED])
        l = CombatOption("prometheus", 0, 0, -1, 1, 0, 0, False, False, False, False, False, [CombatOption.MAIMED])

        if size == Weapon.SMALL:
            if type == Weapon.SWORD:
                self.name = "dagger"
                self.combatOptions.append(s)
            if type == Weapon.AXE:
                self.name = "hand axe"
            if type == Weapon.HAMMER:
                self.name = "hammer"
            if type == Weapon.BOW:
                self.name = "child's bow"
            if type == Weapon.X_BOW:
                self.name = "hand crossbow"

        if size == Weapon.MEDIUM:
            if type == Weapon.SWORD:
                self.name = "sword"
            if type == Weapon.AXE:
                self.name = "axe"
            if type == Weapon.HAMMER:
                self.name = "mace"
            if type == Weapon.BOW:
                self.name = "bow"
            if type == Weapon.X_BOW:
                self.name = "light crossbow"

        if size == Weapon.LARGE:
            if type == Weapon.SWORD:
                self.name = "bastard sword"
                self.combatOptions.append(a)
            if type == Weapon.AXE:
                self.name = "battle axe"
            if type == Weapon.HAMMER:
                self.name = "war hammer"
                self.combatOptions.append(g)
            if type == Weapon.BOW:
                self.name = "long bow"
            if type == Weapon.X_BOW:
                self.name = "crossbow"

        if size == Weapon.HUGE:
            if type == Weapon.SWORD:
                self.name = "giant sword"
            if type == Weapon.AXE:
                self.name = "great axe"
                self.combatOptions.append(a)
            if type == Weapon.HAMMER:
                self.name = "two handed hammer"
                self.combatOptions.append(h)
            if type == Weapon.BOW:
                self.name = "eight foot bow"
            if type == Weapon.X_BOW:
                self.name = "heavy crossbow"

