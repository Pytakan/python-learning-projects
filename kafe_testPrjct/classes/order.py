from classes.product import Product
class Order:
    def __init__(self):
        self.items = {}
    def add_item(self, product_name, product_price, quantity):
        if product_name in self.items:
            self.items[product_name]['quantity'] += quantity
        else:
            self.items[product_name] = {'price': product_price, 'quantity': quantity}
    def exist_in_order(self, product_name):
        if product_name in self.items:
            return self.items[product_name]['quantity']
        return 0
    def display_order(self):
        total = 0
        for product_name, details in self.items.items():
            item_total = details['price'] * details['quantity']
            total += item_total
            print(f"{product_name} - ${details['price']:.2f} x {details['quantity']} = ${item_total:.2f}")
        print(f"Общая сумма: ${total:.2f}")
    def clear_order(self):
        self.items = {}
    def is_empty(self):
        return len(self.items) == 0
    def get_total(self):
        total = 0
        for details in self.items.values():
            total += details['price'] * details['quantity']
        return total