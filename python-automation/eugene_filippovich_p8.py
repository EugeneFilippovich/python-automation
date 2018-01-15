class Store(object):
    pass
passed = ['Banana', 'Apple']

grocery_items_list = []
hardware_items_list = []
class GroceryStore(Store):
    def add_item(self, item):
        if item in passed:
            grocery_items_list.append(item)
        else:
            raise TypeError("Incorrect item")

    def add_items(self, *items):
        grocery_items_list.extend(items)

    def delete_item(self, item):
        if item in grocery_items_list:
            grocery_items_list.remove(item)
        else:
            raise TypeError("Incorrect item")

    def delete_items(self, *items):
        grocery_items_list = [c for c in items if c != items]
        return grocery_items_list




class HardwareStore(Store):
    pass


class Goods(object):
    def __init__(self, price):
        # self.discount_percentage = discount_percentage
        if price > 0:
            self.price = price
        else:
            raise Exception("Incorrect price")

    @property
    def _price(self):
        return self.price

    def freeze_price(self, boolean, value):
        self.boolean = boolean
        if self.boolean == False:
            self.price = value
        else:
            raise ValueError("No access for price changing")

    def set_discount(self, discount_percentage):
        self.discount_percentage = discount_percentage
        print("Discount percentage is : {}% ".format(discount_percentage))
    #

    def reset_discount(self):
        print ("Your discount has been resetted to 0")
        self.discount_percentage = 0







class Food(Goods):
    pass


class Pizza(Food):
    pass


class Cheese(Food):
    pass


class Bread(Food):
    pass


class Avocado(Food):
    pass


class Tools(Goods):
    pass


class Bow(Tools):
    pass


class Shield(Tools):
    pass


class Stuff(Tools):
    pass


class Wheel(Tools):
    pass

# belmarket = GroceryStore()
# bananas = Banana(6)  # create a banana with 6$ price
# strawberry = Strawberry(22)  # create a strawberry with 22$ price
# belmarket.add_item(bananas)
# belmarket.add_item(strawberry)
# print(belmarket.overall_price_no_discount())  # -> outputs 6+22 -> 28
#
# belmarket.remove_item(strawberry)
# strawberry.set_discount(50)
# strawberry.freeze_price(True)
# belmarket.add_item(strawberry)
# print(belmarket.overall_price_no_discount())



b = Goods(44)
b.set_discount(4)
b.reset_discount()
b.freeze_price(False, 42)

s = GroceryStore()
s.add_item('Apple')
s.add_items('args', 'asdfsdf', 'ag')
s.delete_items('args', 'ag')

# belmarket = Goods(42, 4)
#
# belmarket.set_discount(3)
#
# belmarket.reset_discount()

# discount = bananas.discount_percentage(4)
# print (s.__dict__)

print grocery_items_list
