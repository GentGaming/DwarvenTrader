from C_Consumer import Consumer
class Producer(Consumer):
    def __init__(self):
        super().__init__()
        self.productionSkillTree = [] #holds list of (resource , skill)
        self.resourcesProducing = [] #holds list of (resources in production,progress)
        self.stores = [] #holds list of (resource, quantity)
        self.basicProductionSkill = 1
        self.intelligence = 1
        self.mechanicalAptitude = 1
    def produce(self):
        for resource in self.resourcesProducing:
            pass
            #check that stores holds required resources for production
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

