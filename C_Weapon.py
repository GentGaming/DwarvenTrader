from C_Equipment import Equipment
class Weapon(Equipment):
    def __init__(self,type,prefix,suffix,penetration,damageDie,strengthMax,isTwoHanded,range):
        super().__init__(type,prefix,suffix,penetration,damageDie,strengthMax,isTwoHanded,range)