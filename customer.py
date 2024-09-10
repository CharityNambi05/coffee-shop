from entities import Order

class Customer:
    all_customers = []

    def _init_(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Customer name must be a string of 1-15 characters.")
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be a string of 1-15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        max_spent = 0
        aficionado = None
        for customer in cls.all_customers:
            spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if spent > max_spent:
                max_spent = spent
                aficionado = customer
        return aficionado


