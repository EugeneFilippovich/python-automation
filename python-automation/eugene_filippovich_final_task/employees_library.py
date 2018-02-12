from datetime import datetime
import argparse
import sqlite3
import logging
import sys

# File and stdout loggers declaration
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
LOG_FILENAME = "E:\logging\logs.txt"
file_handler = logging.FileHandler(filename=LOG_FILENAME)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('\n %(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
    import cus_module_logger
except ImportError as err:
    print("Unsuccessful import of {} in {}, check your __init__.py file.".format(err, file_name))
    cus_module_logger = None

local_logger = cus_module_logger.custom_logger()

try:
    from builtins import str as user_unicode  # Resolves 'unicode' compatibility issue with python 3.
    import cus_module_beverages
    import cus_module_database
except ImportError as err:
    local_logger.info("Unsuccessful import of {} in {},"
                      " check your __init__.py file.".format(err, file_name))
    cus_module_beverages = None

# Adding handlers to the logger
logger.addHandler(file_handler)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

# Connecting to the DB
connection = sqlite3.connect("C:/sqlite/users.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sale_quantity INTEGER DEFAULT 1,
                  first_name TEXT,
                  last_name TEXT,
                  beverage_type TEXT,
                  extra_ingredients TEXT,
                  beverage_price INTEGER 
                  )""")


class SuppliesPrice(object):
    LATTE = 5.2
    CAPPUCCINO = 4.8
    GINGER_TEA = 5.0
    AMERICANO = 3.0
    ESPRESSO = 2.8
    BLACK_TEA = 2
    GREEN_TEA = 1.8
    COFFEE = 2.4
    MILK = 1.4
    CREAM = 1.8
    HONEY = 1.6
    CINNAMON = 0.4
    GINGER = 1.0
    LEMON = 0.5
    MINT = 0.3
    ORANGE = 0.4
    LIQUOR = 1.3
    NONE = 0


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
        self.last_name = second_name
        self.position = position

    def view_personal_info(self):
        return self.first_name, self.last_name, self.position


class Manager(Employee):
    def __init__(self, first_name, second_name):
        super(Manager, self).__init__(first_name, second_name, position='Manager')

    @staticmethod
    def show_summary():
        for key in SalesList.list.keys():
            sales = SalesList.list[key]
            total = 0
            for sale in sales:
                total = total + sale.__dict__['total_price']
            print(key + ' ' + str(len(sales)) + ' ' + str(round(total, 2)))

    def _check_position(self, authorized_position_):
        try:
            assert self.user_position.lower() == StaffList.__dict__.get(authorized_position_.lower())
        except AssertionError:
            local_logger.info("This action is prohibited for {}, {}."
                              .format(self.user_name, self.user_position))
            exit(0)
        else:
            return True

    # Method that checks if we have such beverage in our menu.
    @staticmethod
    def _check_beverage(beverage_):
        try:
            assert beverage_.lower() in cus_module_beverages.BeverageMenu.__dict__
        except AssertionError:
            local_logger.info("There is no such beverage \'{}\'."
                              .format(beverage_))
            exit(0)
        else:
            return True

    # Hidden method of making a beverage, only when we are going to sell one.
    def _make_a_beverage(self, beverage_to_make, sugar_, cream_, cinnamon_, authorized_position="salesman"):
        beverage = None
        if Staff._check_position(self, authorized_position) and Staff._check_beverage(beverage_to_make):
            if beverage_to_make.lower() == cus_module_beverages.BeverageMenu.tea_name:
                beverage = cus_module_beverages.Tea(sugar_, cream_, cinnamon_)
            if beverage_to_make.lower() == cus_module_beverages.BeverageMenu.coffee_name:
                beverage = cus_module_beverages.Coffee(sugar_, cream_, cinnamon_)
            if beverage_to_make.lower() == cus_module_beverages.BeverageMenu.liquor_name:
                beverage = cus_module_beverages.Liquor(sugar_, cream_, cinnamon_)
            return beverage

    # Method that shows the price of the beverage, WITHOUT creating it.
    def price_of_beverage(self, beverage_price_to_check, authorized_position="salesman"):
        """ 'authorized_position' that used here and bellow,
         allows us to change WHO exactly is able to do things that time."""
        if Staff._check_position(self, authorized_position) and Staff._check_beverage(beverage_price_to_check):
            beverage_price = cus_module_beverages.BeverageMenu.__dict__.get(beverage_price_to_check.lower())

            local_logger.info("The price of \'{}\' is \'{}$\'"
                              .format(beverage_price_to_check, beverage_price))

    # Method that sells beverage and marks the income. It's creating beverage object before the sell.
    def sell_beverage(self, beverage_to_sell_, sugar_=None, cream_=None,
                      cinnamon_=None, authorized_position="salesman"):
        if Staff._check_position(self, authorized_position) and Staff._check_beverage(beverage_to_sell_):
            # Creating a beverage to sell.
            beverage_to_sell = Staff._make_a_beverage(self, beverage_to_sell_, sugar_, cream_, cinnamon_)
            self.earned = beverage_to_sell.beverage_basic_price

            # Checking if customer ordered some of the additional ingredients.
            if beverage_to_sell.sugar:
                self.earned += cus_module_beverages.BeverageMenu.IngredientsPrices.sugar_price
                self.ingredients_added += "sugar "
            if beverage_to_sell.cream:
                self.earned += cus_module_beverages.BeverageMenu.IngredientsPrices.cream_price
                self.ingredients_added += "cream "
            if beverage_to_sell.cinnamon:
                self.earned += cus_module_beverages.BeverageMenu.IngredientsPrices.cinnamon_price
                self.ingredients_added += "cinnamon"

            # Filling the attribute with the name of the beverage sold.
            self.beverage_sold = beverage_to_sell.beverage_name
            local_logger.info("{} has sold \'{}\' for \'{}$\'."
                              .format(self.user_name, beverage_to_sell.beverage_name, self.earned))
            # Saving the "achievements" of current employee in the database, if database is in place.
            cus_module_database.DataBaseWorkaround.safe_sale(self.user_name.lower(),
                                                             self.beverage_sold, self.earned)

    # Method that writes out a receipt if called.
    def receipt(self, authorized_position="salesman"):
        # Checking if customer wants a bill.
        if Staff._check_position(self, authorized_position):
            with open("bill.txt", "w") as bill:
                bill.write("Did you like that \'{}\' with \'{}\'? Pay \'{}$\' or get out!"
                           .format(self.beverage_sold, self.ingredients_added, self.earned))

    # Method that writes down details of a sale into a file with a JSON.
    def write_down(self):
        with io.open('sales.txt', 'a', encoding='utf-8') as outfile:
            outfile.write(user_unicode(json.dumps(self.__dict__, ensure_ascii=False)))
            outfile.write(user_unicode("\n"))

    # Method that reads data from the database, parses and prints it.
    def check_results(self, authorized_position="manager"):
        if Staff._check_position(self, authorized_position):
            data = cus_module_database.DataBaseWorkaround.read_db()
            for (usr, sells, tot) in data:
                print("User: ", usr, "." * (12 - len(usr)), "Sells_total: ",
                      sells, "." * (8 - len(str(sells))), "Value: ", tot)
        else:
            local_logger.info("Only managers can get a spreadsheet.")


class Managers(Staff):
    def __init__(self, name, position):
        super(Managers, self).__init__(name, position)


class Salesmans(Staff):
    def __init__(self, name, position):
        super(Salesmans, self).__init__(name, position)


def create_personnel(name, position):
    """ Method that creates our worker, that will be able to do corresponding things."""
    worker = None
    if position.lower() == StaffList.salesman:
        worker = Salesmans(name, position.lower())
    elif position.lower() == StaffList.manager:
        worker = Managers(name, position.lower())
    else:
        local_logger.info("Personnel was\'t created. No such position {} here".format(position))
        exit(0)
    return worker

class Salesman(Employee):
    def __init__(self, first_name, second_name):
        super(Salesman, self).__init__(first_name, second_name, position='Salesman')
        self.sales = []

# Making beverage
    def make(self, beverage_type, extra_ingredients):
        # preparing beverage with Beverage and Extra_Ingredient input
        beverage = Beverage(beverage_type, extra_ingredients)
        # appending it to list
        SalesList.list.setdefault(self.first_name, []).append(beverage)
        self.save_detailed_bill(beverage)
        oop = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S--%f")[:-3])
        #saving every operation into separate file
        separate_bill_file = open('E:/test/' + self.first_name + ' ' + self.last_name + '_bill_' + oop + '.txt', 'a')
        separate_bill_file.write(
            "%s\t %s\t %s\n " % (datetime.now().strftime("%d-%m-%Y %H:%M"), self.first_name, beverage.__dict__))
        separate_bill_file.close()
        cursor.execute("INSERT INTO employees (beverage_type, extra_ingredients, beverage_price, first_name, last_name) VALUES (?, ?, ?, ?, ?)",
                       [beverage_type1, extra_ingredients1, round(beverage.__dict__['total_price'], 2), self.first_name, self.last_name])

    @staticmethod
    def get_beverage_price(beverage_type, extra_ingredients):
        # view total beverage price
        beverage_price = Beverage(beverage_type, extra_ingredients)
        print(beverage_price.get_total_price())

    # Saving detailed bill to external place - file
    def save_detailed_bill(self, beverage):
        detailed_bill_file = open('E:/detailed.txt', 'a')
        detailed_bill_file.write(
            "%s\t %s\t %s\n " % (datetime.now().strftime("%d-%m-%Y %H:%M"), self.first_name, beverage.__dict__))
        detailed_bill_file.close()

# Adding argparse for CMD
parser = argparse.ArgumentParser()
parser.add_argument('position', help='Login please', type=str)
parser.add_argument('action', help='Choose an action', type=str)
args = parser.parse_args()

def arg_parser():
    parser = argparse.ArgumentParser(
        description='This script is designed to sell beverages.')

    # Adding arguments to our function.
    parser.add_argument(
        '-d', '--new_db', action='store_true', help='Creation of a new DB', )
    parser.add_argument(
        '-n', '--name', type=str, help='Users name', default=None, )
    parser.add_argument(
        '-p', '--position', type=str, help='Users position', default=None, )
    parser.add_argument(
        '-b', '--sell_beverage', type=str, help='Type of beverage to sell', default=None, )
    parser.add_argument(
        '-s', '--add_sugar', action='store_true', help='Add sugar to beverage', )
    parser.add_argument(
        '-c', '--add_cream', action='store_true', help='Add cream to beverage', )
    parser.add_argument(
        '-i', '--add_cinnamon', action='store_true', help='Add cinnamon to beverage', )
    parser.add_argument(
        '-g', '--get_price', type=str, help='Get the price of the beverage', default=None, )
    parser.add_argument(
        '-l', '--bill', action='store_true', help='Safe the bill', )
    parser.add_argument(
        '-a', '--save_sale', action='store_true', help='Save the sale details', )
    parser.add_argument(
        '-u', '--summary', action='store_true', help='Show the summary', )
    return parser


def safe_parser():
    # Array for all arguments passed to script
    args = arg_parser()

    # Return all variable values
    return args.parse_args()

if args.position == 'John' and args.action == 'show_summary':
    manager = Manager('John', 'Snow')
    manager.show_summary()
    logging.info("Logged as " + manager.first_name + " " + manager.last_name)

    cursor.execute("SELECT (first_name) from employees where first_name = 'Hodor'")
    seller1_first_name = cursor.fetchone()
    cursor.execute("SELECT sum(beverage_price) from employees where first_name = 'Hodor'")
    seller1_total_beverage_price = cursor.fetchone()
    cursor.execute("SELECT sum(sale_quantity) from employees where first_name = 'Hodor'")
    seller1_total_sales = cursor.fetchone()

    cursor.execute("SELECT (first_name) from employees where first_name = 'Tyrion'")
    seller2_first_name = cursor.fetchone()
    cursor.execute("SELECT sum(beverage_price) from employees where first_name = 'Tyrion'")
    seller2_total_beverage_price = cursor.fetchone()
    cursor.execute("SELECT sum(sale_quantity) from employees where first_name = 'Tyrion'")
    seller2_total_sales = cursor.fetchone()

    cursor.execute("SELECT sum(sale_quantity) from employees")
    sellers_summary_sales = cursor.fetchone()
    cursor.execute("SELECT sum(beverage_price) from employees")
    sellers_summary_price = cursor.fetchone()
    logging.info(' \n Seller name \t | \t Number of sales \t | \t Total Value ($) \n'
                  '{0} \t | \t \t {1} \t \t | \t {2} \n'
                  '{3} \t | \t \t {4} \t \t | \t {5} \n'
                  '{6} \t \t | \t \t {7} \t \t | \t {8}'
                  .format(seller1_first_name, seller1_total_sales, seller1_total_beverage_price, seller2_first_name,
                          seller2_total_sales, seller2_total_beverage_price, "Total:", sellers_summary_sales, sellers_summary_price))


elif args.position == 'Tyrion' and args.action == 'make_beverage':
    while True:
        salesman = Salesman('Tyrion', 'Lannister')
        logging.info("Logged as " + salesman.first_name + " " + salesman.last_name)
        try:
            beverage_type1 = input().upper()
            extra_ingredients1 = input().upper()
            logging.info("You made: " + beverage_type1 + ' with ' + extra_ingredients1)
            salesman.make(beverage_type1, [extra_ingredients1])
        except NameError:
            beverage_type1 = None
            logging.info('User {} inputted inputted invalid values'.format([salesman.first_name, salesman.last_name]))
        if beverage_type1 is None:
            break

elif args.position == 'Hodor' and args.action == 'Hodor':
    while True:
        salesman = Salesman('Hodor', 'Hodor')
        logging.info('Hodor Hodor Hodor logged')
        try:
            beverage_type1 = input().upper()
            extra_ingredients1 = input().upper()
            salesman.make(beverage_type1, [extra_ingredients1])
            logging.info("You made: " + beverage_type1 + ' with ' + extra_ingredients1)
        except NameError:
            beverage_type1 = None
            logging.info('User {} inputted invalid values'.format([salesman.first_name, salesman.last_name]))

elif args.position == 'Tyrion' and args.action == 'get_price':
    while True:
        salesman = Salesman('Get', 'Price')
        try:
            beverage_type2 = input().upper
            extra_ingredients2 = input().upper
            salesman.get_beverage_price(beverage_type2, [extra_ingredients2])
            logging.info('User {} requested for total price of {} with {}'.format([salesman.first_name, salesman.last_name],
                                                                                  beverage_type2, extra_ingredients2))
        except NameError:
            beverage_type2 = None
            logging.info('User {} inputted inputted invalid values'.format([salesman.first_name, salesman.last_name]))
        if beverage_type2 is None:
            break

if __name__ == '__main__':

    # "Quiet" check on argument for DB creation.
    if parser.new_db:
        cus_module_database.DataBaseWorkaround.create_db_table()

    # Creating user.
    user = cus_module_staff.create_personnel(ArgChecks.check_name(), ArgChecks.check_position())

    # Initiating our additions and selling beverage with or without them if 'user_selling'.
    user_selling = ArgChecks.check_sell()
    if user_selling:
        sugar, cream, cinnamon = ArgChecks.check_additions()
        user.sell_beverage(user_selling, sugar, cream, cinnamon)

        # Allowing billing and filing sale only if we sold a beverage.
        user_billing = ArgChecks.check_bill()
        if user_billing:
            user.receipt()

        user_saving_sale = ArgChecks.check_sales()
        if user_saving_sale:
            user.write_down()

        # Checking if we want to exit.
        ArgChecks.check_exit()

    # Showing the summary of all sales.
    user_summary = ArgChecks.check_summary()
    if user_summary:
        user.check_results()

    # Checking the price of beverage.
    user_checking = ArgChecks.check_price()
    if user_checking:
        user.price_of_beverage(user_checking)

connection.commit()
connection.close()



