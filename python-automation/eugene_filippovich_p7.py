import random
import struct

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


class Petrol(CarProduce):
    def __init__(self, gas_tank=60):
        super(Petrol, self).__init__()
        self.petrol_price = 2.4
        self.mileage_before_repair = 100000
        self.repair_cost = 500
        self.fuel_consumption = 8
        self.gas_tank = gas_tank


class Diesel(CarProduce):
    def __init__(self, gas_tank=60):
        super(Diesel, self).__init__()
        self.diesel_price = 1.8
        self.mileage_before_repair = 150000
        self.repair_cost = 750
        self.fuel_consumption = 6
        self.gas_tank = gas_tank

cars = []

for i in xrange(0, 100):
    gas_tank = 75 if CarProduce.car_id % 5 == 0 else 60
    if CarProduce.car_id % 3 == 0:
        cars.append(Diesel(gas_tank))
    else:
        cars.append(Petrol(gas_tank))

gallons = []
for i in xrange(0, 100):
    gallons.append(cars[i].__dict__['mileage_to_drive'] / (cars[i].__dict__['fuel_consumption']
                   * cars[i].__dict__['gas_tank']))
    cars[i].__dict__['gas_gallons'] = gallons[i]

for i in xrange(0, 100):
    print(cars[i].__dict__)
