from C_Consumer import Consumer
from H_Dictionaries import *
#a = CombatUnit("a",1,1,1)
#b = CombatUnit("b",1,1,1)
#a.myLunge = CombatOption(2,2,2,1,1,1,[],[])
#print (a.myLunge.attackMod)
#print(b.myLunge.attackMod)
masterDic = {}
storesToWant = 0
i=1
c = []
while i < 1001:
    i+=1
    c.append(Consumer())
i =0
for Consumer in c:
    i+=1
    if "Gold" in Consumer.commerceDictionary:
        storesToWant += Consumer.commerceDictionary["Gold"][1]-Consumer.commerceDictionary["Gold"][2]
    dictionaryAddOrSubtract(masterDic, 'dic'+str(i), Consumer.commerceDictionary, 1)
print(storesToWant)