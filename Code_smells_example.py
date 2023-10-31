#Code Smells Example for long method
class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

def is_valid_item(item):
    return item.quantity > 0 and item.price > 100

def calculate_total_price(items):
    total = 0
    for item in items:
        if is_valid_item(item):
            total += item.price * item.quantity
    return total
