def dictionaryAddOrSubtract(dictionary,name,amount,addOrSubtract):
    if addOrSubtract == 1: #add
        if name in dictionary:
            dictionary[name]+=amount
        else:
            dictionary[name]=amount
    elif addOrSubtract == 0: #subtract
        if name in dictionary:
            dictionary[name]-=amount
        else:
            return "Trying to subtract from something that doesn't exist"
    else:
        return "Did not specify add or subtract"
def removeFromDictionary(dictionary,name):
    del dictionary[name]


#make a dictionary with name [stores,want,imoprtance]