import random
import time
from C_ListObject import ListObject

def makeListFromFile(file):
    f = open(file, 'r+')
    contents = f.read()
    contents = contents.replace("*","")
    s = contents.split(',')
    r = random.choice(s)
    if r[0] == " ":
        r = r[1:]
    f.close()
    return r
class Actor(ListObject):
    HUMAN = 1
    ORC = 2
    ELF = 3
    DWARF = 4
    GOBLIN = 5
    MALE = 6,"male"
    FEMALE = 7,"female"
    def __init__(self):
        self.firstName = "should never see this"
        self.lastName = "should never see this"
        self.race = random.randint(1,5)
        if random.randint(1,2) == 1: self.gender = Actor.MALE
        else: self.gender = Actor.FEMALE
        self.createRandomName()
        self.name = self.firstName + " " + self.lastName

    def createRandomName(self):
        g = self.gender[1]
        r = self.getRaceWord()
        path = "names/"
        fn = path+g+r+"FirstNames.txt"
        ln = path+r+"LastNames.txt"
        self.firstName = makeListFromFile(fn)
        self.lastName = makeListFromFile(ln)
    def getRaceWord(self):
        l = ["Human","Orc","Elf","Dwarf","Goblin"]
        return l[self.race-1]
