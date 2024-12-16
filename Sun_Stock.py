class Stock:
    #constructor
    def __init__(self, symbol, name, prevPrice, curPrice):
        self.__symbol = symbol
        self.__name = name
        self.__prevPrice = prevPrice
        self.__curPrice = curPrice

    #getters
    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPrevPrice(self):
        return self.__prevPrice

    def getCurPrice(self):
        return self.__curPrice
    
    #setters
    def setSymbol(self, symbol):
        self.__symbol = symbol

    def setName(self, name):
        self.__name = name

    def setPrevPrice(self, prevPrice):
        self.__prevPrice = prevPrice

    def setCurPrice(self, curPrice):
        self.__curPrice = curPrice

    def getChange(self):
        result = (self.__curPrice - self.__prevPrice) / self.__curPrice
        return round(result *100,2)
