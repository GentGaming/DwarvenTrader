from C_CombatUnit import CombatUnit
from C_CombatOption import CombatOption
a = CombatUnit("a",1,1,1)
b = CombatUnit("b",1,1,1)
a.myLunge = CombatOption(2,2,2,1,1,1,[],[])
print (a.myLunge.attackMod)
print(b.myLunge.attackMod)
