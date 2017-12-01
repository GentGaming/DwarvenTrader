from C_ListObject import ListObject
class Actor(ListObject):
    def __init__(self):
        self.name = createRandomName()

def createRandomName():
    name = "default actor name"
    return name