#laptop routers order warehouse
#relationships: inheritance(polymorphism), aggregation, composition
#warehouse has many routers and laptops -> aggregation
#order has routers and laptops -> aggregation?
#warehouse uses order -> composition
#laptop and router are subclasses of product -> inheritance

class Product:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Laptop(Product):
    def __init__(self, model, price):
        super().__init__(model, price)


class Router(Product):
    def __init__(self, model, price):
        super().__init__(model, price)

class Order:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def __str__(self):
        return ' '.join([str(p) for p in self.products])
    #   retrun self.model + ' @ ' + str(self.price)

class Warehouse:
    def __init__(self, laptops, routers):
        self.laptops = laptops
        self.routers = routers

order = Order()
warehouse = Warehouse([Laptop('mac', 1999)], [Router('netgate', 600)])
order.add_product(warehouse.laptops[0])
print(order)