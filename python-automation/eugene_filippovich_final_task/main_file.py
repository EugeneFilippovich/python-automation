from datetime import datetime
import argparse
import sqlite3
import logging
import sys
from logging.handlers import RotatingFileHandler
from xlsxwriter.workbook import Workbook

# File and stdout loggers declaration
LOG_FILENAME = "E:\logging\logs.txt"
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
file_handler = RotatingFileHandler(filename=LOG_FILENAME, maxBytes=2048, backupCount=10)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('\n %(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
    # Export database to the .xls file
    @staticmethod
    def export_xls():
        workbook = Workbook('E:\logging\output2.xlsx')
        worksheet = workbook.add_worksheet()
        mysel = cursor.execute("SELECT * FROM employees")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        workbook.close()

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
        # saving every operation into separate file
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

# Adding argparse for command line
parser = argparse.ArgumentParser()
parser.add_argument('position', help='Login please', type=str)
parser.add_argument('action', help='Choose an action', type=str)
args = parser.parse_args()


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

elif args.position == 'John' and args.action == 'export_xls':
    manager = Manager('John', 'Snow')
    manager.export_xls()

elif args.position == 'Tyrion' and args.action == 'make_beverage':
    while True:
        salesman = Salesman('Tyrion', 'Lannister')
        logging.info("Logged as " + salesman.first_name + " " + salesman.last_name)
        try:
            beverage_type1 = input().upper()
            extra_ingredients1 = input().upper()
            logging.info("{} {} made {} with {}".format(salesman.first_name, salesman.last_name, beverage_type1, extra_ingredients1))
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
            logging.info("{} {} made {} with {}".format(salesman.first_name, salesman.last_name, beverage_type1, extra_ingredients1))
        except NameError:
            beverage_type1 = None
            logging.info('User {} inputted invalid values'.format([salesman.first_name, salesman.last_name]))

elif args.position == 'Tyrion' and args.action == 'get_price':
    while True:
        salesman = Salesman('Get', 'Price')
        try:
            beverage_type2 = input().upper()
            extra_ingredients2 = input().upper()
            salesman.get_beverage_price(beverage_type2, [extra_ingredients2])
            logging.info('User {} requested for total price of {} with {}'.format([salesman.first_name, salesman.last_name],
                                                                                  beverage_type2, extra_ingredients2))
        except NameError:
            beverage_type2 = None
            logging.info('User {} inputted inputted invalid values'.format([salesman.first_name, salesman.last_name]))
        if beverage_type2 is None:
            break

connection.commit()
connection.close()



