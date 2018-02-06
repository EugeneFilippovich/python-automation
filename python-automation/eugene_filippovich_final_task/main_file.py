# detailed_bill_file = open('E:/detailed.txt', 'w')


class SuppliesPrice(object):
    LATTE = 5.2
    CAPPUCCINO = 4.8
    GINGER_TEA = 5.0
    AMERICANO = 3.0
    ESPRESSO = 2.8
    COFFEE = 2.4
    MILK = 1.4
    CREAM = 1.8
    HONEY = 1.6
    CINNAMON = 0.4
    BLACK_TEA = 2
    GREEN_TEA = 1.8
    GINGER = 1.0
    LEMON = 0.5
    MINT = 0.3
    ORANGE = 0.4
    LIQUOR = 1.3


class Beverage(object):
    def __init__(self, beverage_type, extra_ingredients):
        self.beverage_type = beverage_type
        self.extra_ingredients = extra_ingredients
        self.total_price = self.get_total_price()

    def get_total_price(self):
        total_price = 0
        total_price += SuppliesPrice.__dict__[self.beverage_type]
        for ingredient in self.extra_ingredients:
            total_price += SuppliesPrice.__dict__[ingredient]
        return total_price


class SalesList(object):
    list = {}


class Employee(object):
    def __init__(self, first_name, second_name, position):
        self.first_name = first_name
        self.second_name = second_name
        self.position = position

    def view_personal_info(self):
        return self.first_name, self.second_name, self.position


class Manager(Employee):
    def __init__(self, first_name, second_name):
        super(Manager, self).__init__(first_name, second_name, position='Manager')

    @staticmethod
    def show_summary():
        total = 0
        for i in range(len(SalesList.list)):
            total += i
        print(total)


class Salesman(Employee):
    def __init__(self, first_name, second_name):
        super(Salesman, self).__init__(first_name, second_name, position='Salesman')
        self.sales = []

    def make(self, beverage_type, extra_ingredients):
        beverage = Beverage(beverage_type, extra_ingredients)
        # self.sales.append(beverage)
        SalesList.list.setdefault(self.first_name, []).append(beverage)


    # @staticmethod
    # def save_detailed_bill():
    #     for item in SalesList.list:
    #         detailed_bill_file.write("%s\n" % item)
    #     detailed_bill_file.close()

manager = Manager('John', 'Snow')
salesman = Salesman('Ramsay', 'Bolton')

# print(manager.view_personal_info())
# print(salesman.view_personal_info())
#
# Salesman.make_latte()
# Salesman.make_cappuccino()
# Salesman.make_americano()
# Salesman.make_raf()
# Salesman.make_ginger_tea()
# Salesman.make_green_tea()
# Salesman.make_black_tea()
#
#
# # Salesman.save_detailed_bill()
# print(SalesList.list)
# Manager.show_summary()


salesman.make('LATTE', [])
salesman.make('GREEN_TEA', ['MILK', "GINGER"])

print(SalesList.list.items())
for k in SalesList.list:
    print(k)
    for _ in SalesList.list[k]:
        print(_.__dict__['beverage_type'])
