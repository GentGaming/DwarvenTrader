from C_Equipment import  Equipment
class Armor(Equipment):
    LIGHT = 1
    MEDIUM = 2
    HEAVY = 3

    def __init__(self,prefix,suffix,type,armourValue,dodgeValue):
        light_type = ["leather", "studded leather", "padded armor"]
        medium_type = [] # fill in
        heavy_type = [] # fill in
        super().__init__()

