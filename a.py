class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
    def get_deal_price(self):
        return self.deal_price
    
    def display_product_details(self):
        print("{} {}".format(self.name,self.price))
        
class Electronicdevice(Product):
    def set_waranty(self,waranty_in_months):
        self.waranty_in_months = waranty_in_months
    def get_waranty(self):
        return self.waranty_in_months
    def display_product_details(self):
        super().display_product_details()  # Call the parent class's method
        print("Waranty: {} months".format(self.waranty_in_months))
        
tv = Electronicdevice("TV",10000,50000,3.5)
tv.set_waranty(24)
order = Order("prine_delivery","Hyderabad")
order.add_item(tv,1)
order.display_order_details()
        