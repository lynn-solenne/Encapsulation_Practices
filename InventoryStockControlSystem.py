class Inventory:
    def __init__(self,product_name,stock):
        self.__product_name=product_name
        self.__stock=stock
    #getter
    def get_stock(self):
        return self.__stock
   #setter
    def set_stock(self,quantity):
        if quantity >= 0:
            self.__stock=quantity
        else:
            print("Invalid stock!")
    def sell(self,quantity):
        if quantity > self.__stock:
            print(f"Insufficient stock!")
        else:
            self.__stock -= quantity

    def restock(self,quantity):
        if quantity >= 0:
            self.__stock += quantity

        else:
            print("Invalid quantity!")

p=Inventory("Laptop",20)
p.sell(8)
print(p.get_stock())
p.sell(15)
p.restock(10)
print(p.get_stock())
p.set_stock(-5)
print(p.get_stock())
