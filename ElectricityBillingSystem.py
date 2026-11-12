class ElectricityBill:
    def __init__(self,units):
        self.__units=units
    @property
    def units(self):
        return self.__units
    @units.setter
    def units(self,unit):
       if unit <0:
           print("Invalid units!")
       else:
           self.__units =unit
    @property
    def total_bill(self):
        if self.__units<= 100:
            return self.__units * 5
        elif self.__units <= 200:
            return (100*5)+ ((self.__units-100 )* 7)
        else:
            return (100*5)+(100*7)+ ((self.__units-200 )* 10)
bill= ElectricityBill(80)
print(bill.total_bill)
bill.units=250
print(bill.total_bill)
bill.units=-10
print(bill.units)

