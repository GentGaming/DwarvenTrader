from C_Resource import Resource
import random

class WorldController:
    def __init__(self):
        self.worldResources = self.createWorldResources()

    def createWorldResources(self):
        self.worldResources = []
        # this is called once
        resourceTypes = ["Gold", "Iron", "Silver", "Food", "Water"]
        for i in range(5):
            chosenResource = random.choice(resourceTypes)
            self.worldResources.append(Resource(chosenResource,0,0,0,0,0))
            resourceTypes.remove(chosenResource)
        return self.worldResources
god = WorldController()
print(god.worldResources)



