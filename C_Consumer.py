from C_Actor import Actor
import random

class Consumer(Actor):
    def __init__(self):
        self.stores = []
        self.commerceDictionary = {} #holds list of resource , consumption rate per 100 ticks
        self.populateCommerce()
    def populateCommerce(self):
        resourceTypes = ["Gold", "Iron", "Silver", "Food", "Water"]
        i=0
        while i < 3:
            chosenResource = random.choice(resourceTypes)
            self.commerceDictionary[chosenResource] = 0,random.randint(50,100),random.randint(1,100)
            resourceTypes.remove(chosenResource)
            i+=1
    def update(self):
        pass

