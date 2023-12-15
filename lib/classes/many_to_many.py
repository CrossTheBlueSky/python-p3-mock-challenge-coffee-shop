class Coffee:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) is str and 0 < len(name) <=15:
            self._name = name
        else:
            print("Follow the naming conventions")

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee == self})
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        count = 0
        total = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
                total += order.price
        if count == 0:
            return 0
        else:
            return total/count

class Customer:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) is str and 0 < len(name) <= 15:
            self._name = name
        else:
            print("Wrongo")

    name = property(get_name, set_name)
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):

     return list({order.coffee for order in Order.all if order.customer == self})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        spenders = {}
        current = None
        big_spender = None
        big_total = 0

        for order in Order.all:
            if order.coffee is coffee:
                total = 0
                current = order.customer
                print(f"{order.price}")

                if f"{current}" in spenders:                        
                    current_total = spenders[f"{current}"]
                    print(f"{current.name} in spenders. Current total = {current_total}")
                    total = spenders[f"{current}"] + order.price
                    spenders[f"{current}"] = total
                    print(f"{current.name} new Total is:")
                    print(spenders[f"{current}"])
                    print(total)
                else:
                    spenders[f"{current}"] = order.price
                    total = order.price
    
                if big_spender == None:
                    print("No Big Spender. Setting Big Spender to:")
                    print(f"{current.name} with a total of {total}")
                    big_spender = current
                    big_total = total
                elif big_total < total:
                    print(f"{current.name} has spent more than {big_spender.name} with {total}")
                    big_spender = current
                    big_total = total
                
        return big_spender





    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    def get_price(self):
        return self._price

    def set_price(self, price):
        if type(price) is float and hasattr(self, "price") != True and 1.0 <= price <= 10.0:
            self._price = price
        else:
            print("Just do it right, jeez")

    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        if type(customer) is Customer:
            self._customer = customer
        else:
            print("This ain't a customer, bub")

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self, coffee):
        if type(coffee) is Coffee:
            self._coffee = coffee
        else:
            print("We only serve the good stuff here")
    