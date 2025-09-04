class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        return f"{self.name} - ${self.price:.2f}"

    def get_price(self):
        return self.price
    def get_name(self):
        return self.name