import random


class Fuel():
    PETROL_92 = 2.2
    PETROL_95 = 2.4
    DIESEL = 1.8


class CarService():
    PETROL_REPAIR_COST = 500
    DIESEL_REPAIR_COST = 700
    ENGINE_REPLACE = 3000

FUEL_CONSUMPTION_INCREASE = 0.01
CHECK_DISTANCE = 1000
TOTAL_CARS_COUNT = 100


class CarProduce(object):
    car_id = 1

    def __init__(self):
        print("Creating new car {}".format(id(self)))
        self.car_id = CarProduce.car_id
        CarProduce.car_id += 1
        self.start_price = 10000
        self.gas_tank = 60
        self.total_mileage = 0
        self.fuel_consumption = 0
        self.gas_gallons = 0
        self.mileage_to_drive = random.randint(55000, 286000)
        self.reduce_price = 0
        self.total_fuel = 0
        self.repair_count = 0
        self.total_credit = 0
        self.fuel = 'PETROL_92'

    def mileage_increase(self, distance=0):
        if distance > 0:
            self.total_mileage += distance

    def info(self):
        print('mycar')


class Petrol(CarProduce):
    def __init__(self, gas_tank=60):
        super(Petrol, self).__init__()
        self.mileage_before_repair = 100000
        self.fuel_consumption = 8
        self.gas_tank = gas_tank
        self.reduce_price = 9.5
        self.fuel = 'PETROL_92'

    def info(self):
        print('PETROL', self.__dict__)

    def change_petrol_price(self):
        self.fuel = 'PETROL_95' if (self.total_mileage >= 50000) else 'PETROL_92'


class Diesel(CarProduce):
    def __init__(self, gas_tank=60):
        super(Diesel, self).__init__()
        self.mileage_before_repair = 150000
        self.fuel_consumption = 6
        self.gas_tank = gas_tank
        self.reduce_price = 10.5
        self.fuel = 'DIESEL'

    def info(self):
        print('DIESEL', self.__dict__)

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

    if isinstance(cars[i], Petrol):
        repair_cost = CarService.PETROL_REPAIR_COST
    elif isinstance(cars[i], Diesel):
        repair_cost = CarService.DIESEL_REPAIR_COST
    else:
        repair_cost = 0

    for j in xrange(0, cars[i].mileage_to_drive, CHECK_DISTANCE):
        remain_to_drive = cars[i].mileage_to_drive - cars[i].total_mileage

        DISTANCE = CHECK_DISTANCE if (remain_to_drive >= CHECK_DISTANCE) else remain_to_drive

        if isinstance(cars[i], Petrol):
            cars[i].change_petrol_price()

        if remain_before_repair < DISTANCE:
            if (cars[i].start_price - repair_cost) <= 0:
                continue
            cars[i].start_price -= repair_cost
            cars[i].repair_count += 1
            remain_before_repair = cars[i].mileage_before_repair - (DISTANCE - remain_before_repair)
        else:
            remain_before_repair -= DISTANCE

        if cars[i].start_price <= 0:
            cars[i].start_price -= CarService.ENGINE_REPLACE
            cars[i].total_credit += cars[i].start_price
            break

        cars[i].mileage_increase(DISTANCE)
        cars[i].total_fuel += (DISTANCE * cars[i].fuel_consumption / 100)
        cars[i].start_price -= ((cars[i].fuel_consumption * Fuel.__dict__[cars[i].fuel] * DISTANCE / 100) + cars[i].reduce_price)
        cars[i].fuel_consumption += cars[i].fuel_consumption * FUEL_CONSUMPTION_INCREASE
        #
        if cars[i].start_price <= 0:
            cars[i].total_credit += (cars[i].start_price * (-1) + CarService.ENGINE_REPLACE)
        total_credit_to_pay += cars[i].total_credit


for i in xrange(0, TOTAL_CARS_COUNT):
    print(cars[i].info(), cars[i].fuel)

print('Total credit to pay = ' + str(total_credit_to_pay))

# car1 = CarProduce()
#
# car1.info()



print(cars[i].__dict__, Fuel.__dict__[cars[i].fuel])