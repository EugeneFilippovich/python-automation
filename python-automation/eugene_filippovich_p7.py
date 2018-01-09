import random

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

    def info(self):
        print(self.total_mileage, self.start_price, self)


class Petrol(CarProduce):
    def __init__(self, gas_tank=60):
        super(Petrol, self).__init__()
        self.petrol_price = 2.4
        self.mileage_before_repair = 100000
        self.repair_cost = 500
        self.fuel_consumption = 8
        self.gas_tank = gas_tank
        self.reduce_price = 9.5


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

for i in xrange(0, 100):
    gas_tank = 75 if CarProduce.car_id % 5 == 0 else 60
    if CarProduce.car_id % 3 == 0:
        cars.append(Diesel(gas_tank))
    else:
        cars.append(Petrol(gas_tank))

gallons = []
for i in xrange(0, 100):
    gallons.append(cars[i].mileage_to_drive / (cars[i].fuel_consumption
                   * cars[i].gas_tank))
    cars[i].gas_gallons = gallons[i]

for i in xrange(0, len(cars)):
    remain_before_repair = cars[i].mileage_before_repair

    for j in xrange(0, cars[i].mileage_to_drive, 1000):

        remain_to_drive = cars[i].mileage_to_drive - cars[i].total_mileage

        DISTANCE = 1000 if (remain_to_drive >= 1000) else remain_to_drive

        if remain_before_repair < DISTANCE:
            if (cars[i].start_price - cars[i].repair_cost) <= 0:
                break
            cars[i].start_price -= cars[i].repair_cost
            cars[i].repair_count += 1
            remain_before_repair = cars[i].mileage_before_repair - (DISTANCE - remain_before_repair)
        else:
            remain_before_repair -= DISTANCE

        if cars[i].start_price <= 0:
            break
        # if cars[i].mileage_before_repair >= cars[i].total_mileage:
        #     cars[i].start_price = cars[i].start_price - cars[i].repair_cost
        # if cars[i].start_price <= 0:
        #     break
        cars[i].total_mileage += DISTANCE
        cars[i].total_fuel += (DISTANCE * cars[i].fuel_consumption / 100)
        cars[i].start_price -= ((cars[i].fuel_consumption * cars[i].petrol_price) + cars[i].reduce_price)
        cars[i].fuel_consumption += cars[i].fuel_consumption * 0.01

for i in xrange(0, 100):
    print(cars[i].__dict__)

# car1 = CarProduce()
#
# car1.info()
