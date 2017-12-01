from H_Commerce_Functions import askForItemFromList
class CustomsAgent:
    def __init__(self,employer):
        self.employer = employer

    def determinePrices(self):
        prices = []
        for good in self.employer.stores:

            prices.append(good,self.getSellPriceOfGood(good),self.getBuyPriceOfGood())
        return prices
    def getSellPriceOfGood(self, good):
        price = 1

        return price

    def getBuyPriceOfGood(self, good):
        price = 1

        return price
    def offerGoods(self):
        goods = self.determinePrices()
        askForItemFromList(goods)
