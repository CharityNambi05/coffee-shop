from entities import Coffee, Customer

coffee1 = Coffee("Espresso")
customer1 = Customer("Joy")

order1 = customer1.create_order(coffee1, 4.5)

print(f"{customer1.name} ordered {coffee1.name} for ${order1.price}")
print(f"Total orders for {coffee1.name}: {coffee1.num_orders()}")
print(f"Average price for {coffee1.name}: {coffee1.average_price()}")
