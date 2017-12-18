from C_Producer import Producer
from C_Consumer import Consumer
from C_CustomsAgent import CustomsAgent
from C_Map_Object import Map_Object
class Stronghold:
    def __init__(self, name):
        self.name = name
        #super().__init__(name)
        self.producers = []
        self.consumers = []
        self.populate2()
        self.agent = CustomsAgent(self)
        '''
        self.populate(self.producers,Producer())
        self.populate(self.consumers,Consumers())
        '''
    def populate(self,thingToPopulate,whatAmIPopulating):
        i = 1
        thingToPopulate = []
        while i < 1001:
            i += 1
            thingToPopulate.append(whatAmIPopulating)
    def populate2(self):
        for i in range(1000):
            self.producers.append(Producer())
            self.consumers.append(Consumer())