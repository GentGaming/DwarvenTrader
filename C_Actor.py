from C_ListObject import ListObject
class Actor(ListObject):
    def __init__(self):
        self.name = createRandomName()
        self.strength = 1
        self.speed = 1
        self.awareness = 1

def createRandomName():
    name = "default actor name"
    return name