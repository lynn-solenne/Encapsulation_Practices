class BusTicket:
    def __init__(self,age,distance):
        self.__age=age
        self.__distance=distance
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if 0< value <=120:
           self.__age=value
        else:
            print("Invalid age!")
    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self,value):
        if value>0:
           self.__distance= value
        else:
            print("Invalid distance!")
    @property
    def fare(self):
        baseFare=10
        total=baseFare+(self.distance*5)
        if self.__age<= 5:
            return total *0
        elif 6<= self.__age <= 12:
            return total *0.5
        elif self.__age >= 60:
            return total * 0.5
        else:
            return total *1
ticket=BusTicket(25,10)
print(ticket.fare)
ticket.age=65
print(ticket.fare)
ticket.distance=-5
print(ticket.fare)
ticket.age=4
print(ticket.fare)

# while we need to use setters to age and distance to update informations, fare is read-only cause
# fare should be calculated  automatically based on age and distance to prevent ticket price changing manually