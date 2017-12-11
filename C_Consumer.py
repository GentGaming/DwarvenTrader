from C_Actor import Actor
class Consumer(Actor):
    def __init__(self):
        self.stores = []
        self.consumedResources = [] #holds list of resource , consumption rate per 100 ticks
        self.desiredResources = [] #holds list of resources, quantity, entered in order of importance?

    def update(self):
        pass