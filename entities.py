# entities.py

class Coffee:
    coffee_list = []

    def __init__(self, name):
        self.name = name
        self.orders = []
        Coffee.coffee_list.append(self)

    def create_order(self, customer, price):
        order = Order(customer, self, price)
        self.orders.append(order)
        return order

    def num_orders(self):
        return len(self.orders)

    def average_price(self):
        if not self.orders:
            return 0
        return sum(order.price for order in self.orders) / len(self.orders)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def create_order(self, coffee, price):
        order = coffee.create_order(self, price)
        self.orders.append(order)
        return order

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
