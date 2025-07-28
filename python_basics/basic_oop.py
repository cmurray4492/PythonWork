"""Basic OOP from Ashutosh Pawar Python course"""


class Product:
    quantity = 200

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def summer_discount(self, discount_percent):
        self.price = self.price - (self.price * discount_percent/100)


p3 = Product("Tshirt", 10)
print(p3.name)
print(p3.price)

p3.summer_discount(10)

print(p3.name)
print(p3.price)


p1 = Product("phone", 300)
print(f"Quantity In Stock:  {p1.quantity}")
print(f"Product Name: {p1.name}")
print(f"Current Price: {p1.price}")
p1.summer_discount(50)
print(f"Discount Price: {p1.price}")

print('----------------------')

p2 = Product("laptop", 900)
print(f"Quantity In Stock:  {p2.quantity}")
print(f"Product Name: {p2.name}")
print(f"Current Price: {p2.price}")
p2.summer_discount(25)
print(f"Discount Price: {p2.price}")
