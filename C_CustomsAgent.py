from H_Commerce_Functions import askForItemFromList
from C_World_Controller import WorldController

class CustomsAgent:
    def __init__(self,employer):
        self.employer = employer

    def determineDemandForGood(self,good):
        #total demand = want-stores-producers stores of selling(stores-wants)
        storesToWantP = 0
        storesToWantC = 0
        for Producer in self.employer.producers:
            if good in Producer.commerceDictionary:
                a = Producer.commerceDictionary[good][0] - Producer.commerceDictionary[good][1]
                if a>0: storesToWantP+=a

        for Consumer in self.employer.consumers:
            if good in Consumer.commerceDictionary:
                storesToWantC += Consumer.commerceDictionary[good][1] - Consumer.commerceDictionary[good][0]
        totalDemand = storesToWantC-storesToWantP
        return totalDemand

    def determinePrices(self,good,amount):
        prices = {"Food":10}
        return prices[good], prices[good]*amount
    def getSellPriceOfGood(self, good):
        price  = 1

        return price

    def getBuyPriceOfGood(self, good):
        price = 1

        return price
    def removeItemsThatWereTradedInHouse(self,allGoods):
        pass
    def offerGoods(self):
        goods = self.determinePrices()
        askForItemFromList(goods)
