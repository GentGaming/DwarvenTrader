from C_Consumer import Consumer
from H_Dictionaries import dictionaryAddOrSubtract
import random
class Producer(Consumer):
    def __init__(self):
        super().__init__()
        self.productionSkillTree = [] #holds list of (resource , skill)
        self.resourcesProducing = [] #holds list of (resources in production,progress)
        self.stores = [] #holds list of (resource, quantity)
        self.basicProductionSkill = 1
        self.intelligence = 1
        self.mechanicalAptitude = 1
        self.commerceDictionary["Food"] = 300, random.randint(50, 100), random.randint(1, 100)

    def produce(self):

        for resource in self.resourcesProducing:
            # check that stores holds required resources for production
            for component in resource.components:
                if not self.stores.__contains__(component):
                    self.send("not enough resources")
                #progress resources in production based on skill and basicProductionSkill
                #remove resources from store used in production
                #chance to improve skill
                    #include intelligence and mechanicalAptitude if appropriate (should be flushed out more)
    def setWholeSalePrices(self):
        for resource in self.stores:
            if self.resourcesProducing.__contains__(resource):
                #resource is for sale set a price and return
                #list of resources for sale
                pass

