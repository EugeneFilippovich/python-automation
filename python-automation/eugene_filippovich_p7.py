import random


class Fuel():
    PETROL_PRICE = 2.4
    DIESEL_PRICE = 1.8
    FUEL_CONSUMPTION_INCREASE = 0.01

class CarService():
    PETROL_REPAIR_COST = 500
    DIESEL_REPAIR_COST = 700
    ENGINE_REPLACE = 3000


CHECK_DISTANCE = 1000
TOTAL_CARS_COUNT = 100


class CarProduce(object):
    car_id = 1
    fuel_consumption = None

    def __init__(self):
        print("Creating new car {}".format(id(self)))
        self.car_id = CarProduce.car_id
        CarProduce.car_id += 1
        self.start_price = 10000
        self.gas_tank = 60
        self.total_mileage = 0
        self.fuel_consumption = CarProduce.fuel_consumption
        self.gas_gallons = 0
        self.mileage_to_drive = random.randint(55000, 286000)
        self.reduce_price = 0
        self.total_fuel = 0
        self.repair_count = 0
        self.replace_engine = 3000
        self.total_credit = 0

    def mileage_increase(self, distance=0):
        if distance > 0:
            self.total_mileage += distance

    # def recount_car_price(self, price=0):

    # def info(self):
    #     print(self.total_mileage, self.start_price, self)


class Petrol(CarProduce):
    def __init__(self, gas_tank=60):
        super(Petrol, self).__init__()
        self.petrol_price = 2.2
        self.mileage_before_repair = 100000
        self.repair_cost = 500
        self.fuel_consumption = 8
        self.gas_tank = gas_tank
        self.reduce_price = 9.5

    def change_petrol_price(self):
        self.petrol_price = 2.4 if (self.total_mileage >= 50000) else 2.2


class Diesel(CarProduce):
    def __init__(self, gas_tank=60):
        super(Diesel, self).__init__()
        self.petrol_price = 1.8
        self.mileage_before_repair = 150000
        self.repair_cost = 750
        self.fuel_consumption = 6
        self.gas_tank = gas_tank
        self.reduce_price = 10.5

cars = []

for i in xrange(0, TOTAL_CARS_COUNT):
    gas_tank = 75 if CarProduce.car_id % 5 == 0 else 60
    if CarProduce.car_id % 3 == 0:
        cars.append(Diesel(gas_tank))
    else:
        cars.append(Petrol(gas_tank))

gallons = []

for i in xrange(0, TOTAL_CARS_COUNT):
    gallons.append(cars[i].mileage_to_drive / (cars[i].fuel_consumption * cars[i].gas_tank))
    cars[i].gas_gallons = gallons[i]

total_credit_to_pay = 0
for i in xrange(0, len(cars)):
    remain_before_repair = cars[i].mileage_before_repair

    for j in xrange(0, cars[i].mileage_to_drive, CHECK_DISTANCE):
        remain_to_drive = cars[i].mileage_to_drive - cars[i].total_mileage

        DISTANCE = CHECK_DISTANCE if (remain_to_drive >= CHECK_DISTANCE) else remain_to_drive

        if isinstance(cars[i], Petrol):
            cars[i].change_petrol_price()

        if remain_before_repair < DISTANCE:
            if (cars[i].start_price - cars[i].repair_cost) <= 0:
                continue
            cars[i].start_price -= cars[i].repair_cost
            cars[i].repair_count += 1
            remain_before_repair = cars[i].mileage_before_repair - (DISTANCE - remain_before_repair)
        else:
            remain_before_repair -= DISTANCE

        if cars[i].start_price <= 0:
            cars[i].start_price -= cars[i].replace_engine
            break

        cars[i].mileage_increase(DISTANCE)
        # cars[i].total_mileage += DISTANCE
        cars[i].total_fuel += (DISTANCE * cars[i].fuel_consumption / 100)
        cars[i].start_price -= ((cars[i].fuel_consumption * cars[i].petrol_price * DISTANCE / 100) + cars[i].reduce_price)
        cars[i].fuel_consumption += cars[i].fuel_consumption * Fuel.FUEL_CONSUMPTION_INCREASE

        if cars[i].start_price <= 0:
            cars[i].total_credit += (cars[i].start_price * (-1) + cars[i].replace_engine)
        total_credit_to_pay += cars[i].total_credit


for i in xrange(0, TOTAL_CARS_COUNT):
    print(cars[i].__dict__)

print('Total credit to pay = ' + str(total_credit_to_pay))

# car1 = CarProduce()
#
# car1.info()
