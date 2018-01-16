class Store(object):
    pass

passed = ['Banana', 'Apple', 'Pizza']

grocery_items_list = []

hardware_items_list = []


class GroceryStore(Store):
    goods_list = []

    def add_item(self, item):
        if isinstance(item, Food):
            self.goods_list.append(item)

    def add_items(self, *items):
        self.goods_list.extend(items)

    def delete_item(self, item):
        if item in self.goods_list:
            self.goods_list.remove(item)
        else:
            raise TypeError("Incorrect item")

    def delete_items(self, *items):
        for item in items:
            if item in self.goods_list:
                self.goods_list.remove(item)

    def info(self):
        for good in self.goods_list:
            print (good.__dict__)


class HardwareStore(Store):
    pass


class Goods(object):
    freezed = False

    def __init__(self, price):
        # self.discount_percentage = discount_percentage
        if price > 0:
            self.price = price
        else:
            raise Exception("Incorrect price")

    @property
    def _price(self):
        return self.price

    def set_price(self, price):
        if self.freezed == False:
            self.price = price
        else:
            raise Exception("Price can't be changed")

    def freeze_price(self, is_freezed):
        self.freezed = is_freezed

    def set_discount(self, discount_percentage):
        if self.freezed == False:
            self.discount_percentage = discount_percentage
            print("Discount percentage is : {}% ".format(discount_percentage))
        else:
            raise Exception("Discount can't be applied")
    #

    def reset_discount(self):
        print ("Your discount has been resetted to 0")
        self.discount_percentage = 0


class Food(Goods):
    pass


class Pizza(Food):
    def __init__(self, price):
        self.name = 'Pizza'
        super(Pizza, self).__init__(price)
    pass


class Cheese(Food):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Cheese, self).__init__(price)
    pass


class Bread(Food):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Bread, self).__init__(price)
    pass



class Avocado(Food):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Avocado, self).__init__(price)
    pass



class Tools(Goods):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Tools, self).__init__(price)
    pass



class Bow(Tools):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Bow, self).__init__(price)
    pass



class Shield(Tools):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Shield, self).__init__(price)
    pass



class Stuff(Tools):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Stuff, self).__init__(price)
    pass



class Wheel(Tools):
    def __init__(self, price):
        self.name = 'Cheese'
        super(Wheel, self).__init__(price)
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
b.freeze_price(False)
b.set_price(42)

s = GroceryStore()
p = Pizza(6)
p1 = Cheese(8)
s.add_items(p, p1)
s.delete_items(p, p1)

# print (p.__dict__)


# belmarket = Goods(42, 4)
#
# belmarket.set_discount(3)
#
# belmarket.reset_discount()

# discount = bananas.discount_percentage(4)
# print (s.__dict__)

s.info()
