class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    

product1 = Product("shampoo", 10)
print(product1.title)
print(product1.price)

product2 = Product("conditioner", 5)
print(product2.title)
print(product2.price)
