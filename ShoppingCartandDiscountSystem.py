class ShoppingCart:
    def __init__(self):
        self.__subtotal=0
        self.__discount=0
    def add_item(self,price,quantity):
        if quantity < 0 and price <0:
            print("Invalid price or quantity!")
        else:
            self.__subtotal +=price * quantity

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self,percentages):
        if 0 <= percentages <= 30:
           self.__discount= percentages

        else:
            print("Invalid discount!")
    @property
    def total(self):
         return self.__subtotal*(1-self.discount/100)

cart=ShoppingCart()
cart.add_item(1000,2)
cart.add_item(500,1)
cart.discount=20
print(cart.total)
cart.discount=40
cart.add_item(200,1)
print(cart.total)

