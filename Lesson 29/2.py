class coputer:
    def __init__(self):
        self.__maxmaxprice = 165489299090
    def sell(self):
        print("selling price", self.__maxmaxprice)
    def setmaxprice(self, price):
        self.__maxmaxprice = price
c = coputer()
c.sell()   
c.__maxmaxprice = 100000 # pyright: ignore[reportAttributeAccessIssue]
c.sell()
c.setmaxprice(100000)
c.setmaxprice(100000)
c.sell()