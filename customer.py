from order import Order

class Customer:
    
    def __init__(self, name):
        self.name = name 
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        highest = None
        max_spent = 0
        for customer in set(order.customer for order in coffee.orders()):
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            
            if total > max_spent:
                max_spent = total
                highest = customer
        return highest
    
class About:
    pass    
