class Vehicle:
    #instanciate
    def __init__(self, year, price):
        self.year = year
        self.price = price
    
    
class Car(Vehicle):
    #instanciate
    def __init__(self, year, price):
        self.year = year
        self.price = price   
    #default value for car     
    wheel_count=4
    capacity=4
    def pay_tax(self):
        return (15/100)*self.price
    def park(self, hour):
        cost = 250*self.wheel_count*hour
        if self.capacity>5:
            cost = cost + 5000
        return cost

class Motorbike(Vehicle):
    #instanciate
    def __init__(self, year, price):
        self.year = year
        self.price = price   
    #default value for motorbike
    wheel_count=2
    capacity=2
    def pay_tax(self):
        return (10/100)*self.price
    def park(self, hour):
        cost = 250*self.wheel_count*hour
        if self.capacity>5:
            cost = cost + 5000
        return cost

class Bicycle(Vehicle):
    #instanciate
    def __init__(self, year, price):
        self.year = year
        self.price = price
    #default value for bicycle    
    wheel_count=2
    capacity=1
    def park(self, hour):
        cost = 250*self.wheel_count*hour
        if self.capacity>5:
            cost = cost + 5000
        return cost
    