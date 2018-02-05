# detailed_bill_file = open('E:/detailed.txt', 'w')


class SuppliesPrice(object):
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


class SalesList(object):
    list = []


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

    @staticmethod
    def make_latte(*args):
        latte_price = format(SuppliesPrice.COFFEE + SuppliesPrice.MILK*2 + sum(args), '.2f')
        SalesList.list.append(latte_price)

    @staticmethod
    def make_cappuccino(*args):
        cappuccino_price = format(SuppliesPrice.COFFEE*2 + SuppliesPrice.MILK + sum(args), '.2f')
        SalesList.list.append(cappuccino_price)

    @staticmethod
    def make_americano(*args):
        americano_price = format(SuppliesPrice.COFFEE + sum(args), '.2f')
        SalesList.list.append(americano_price)

    @staticmethod
    def make_raf(*args):
        raf_price = format(SuppliesPrice.COFFEE + SuppliesPrice.MILK + SuppliesPrice.CREAM + SuppliesPrice.LIQUOR + sum(args), '.2f')
        SalesList.list.append(raf_price)

    @staticmethod
    def make_ginger_tea(*args):
        ginger_tea_price = format(SuppliesPrice.LEMON + SuppliesPrice.HONEY + SuppliesPrice.GINGER +
                                  SuppliesPrice.ORANGE + SuppliesPrice.CINNAMON + SuppliesPrice.MINT + sum(args), '.2f')
        SalesList.list.append(ginger_tea_price)

    @staticmethod
    def make_green_tea(*args):
        green_tea_price = format(SuppliesPrice.GREEN_TEA + sum(args), '.2f')
        SalesList.list.append(green_tea_price)

    @staticmethod
    def make_black_tea(*args):
        black_tea_price = format(SuppliesPrice.BLACK_TEA + sum(args), '.2f')
        SalesList.list.append(black_tea_price)

    # @staticmethod
    # def save_detailed_bill():
    #     for item in SalesList.list:
    #         detailed_bill_file.write("%s\n" % item)
    #     detailed_bill_file.close()

manager = Manager('John', 'Snow')
salesman = Salesman('Ramsay', 'Bolton')

print(manager.view_personal_info())
print(salesman.view_personal_info())

Salesman.make_latte()
Salesman.make_cappuccino()
Salesman.make_americano()
Salesman.make_raf()
Salesman.make_ginger_tea()
Salesman.make_green_tea()
Salesman.make_black_tea()


# Salesman.save_detailed_bill()
print(SalesList.list)
Manager.show_summary()
