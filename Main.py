from C_Consumer import Consumer
from H_Dictionaries import *
from C_Stronghold import Stronghold
#a = CombatUnit("a",1,1,1)
#b = CombatUnit("b",1,1,1)
#a.myLunge = CombatOption(2,2,2,1,1,1,[],[])
#print (a.myLunge.attackMod)
#print(b.myLunge.attackMod)
masterDic = {}
storesToWant = 0

s = Stronghold("a")
a = s.agent.determineDemandForGood("Food")
p = s.agent.determinePrices("Food", a)
print(p)