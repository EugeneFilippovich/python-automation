import random


class FuelPrice(object):
    PETROL_92 = 2.2
    PETROL_95 = 2.4
    DIESEL = 1.8


class CarServicePrice(object):
    PETROL_REPAIR_COST = 500
    DIESEL_REPAIR_COST = 700
    ENGINE_REPLACE = 3000


FUEL_CONSUMPTION_INCREASE = 0.01
CHECK_DISTANCE = 1000
TOTAL_CARS_COUNT = 100


class CarFactory(object):
    car_id = 1

    def __init__(self):
        print("Creating new car {}".format(id(self)))
        self.car_id = CarFactory.car_id
        self.start_price = 10000
        self.gas_tank = 60
        self._total_mileage = 0
        self.fuel_consumption = 0
        self.gas_gallons = 0
        self.mileage_to_drive = random.randint(55000, 286000)
        self.reduce_price = 0
        self.total_fuel = 0
        self.repair_count = 0
        self.total_credit = 0
        self.fuel = 'PETROL_92'
        self.total_fuel_cost = 0
        self.gas_gallons_used = 0
        self.mileage_before_util = 0
        CarFactory.car_id += 1

    @property
    def total_mileage(self):
        return self._total_mileage

    def mileage_increase(self, distance=0):
        if distance > 0:
            self._total_mileage += distance

    def info(self):
        print('mycar')


class PetrolCarProduce(CarFactory):
    def __init__(self, gas_tank=60):
        super(PetrolCarProduce, self).__init__()
        self.mileage_before_repair = 100000
        self.fuel_consumption = 8
        self.gas_tank = gas_tank
        self.reduce_price = 9.5
        self.fuel = 'PETROL_92'

    def info(self):
        print('PETROL', self.__dict__)

    def change_petrol_price(self):
        self.fuel = 'PETROL_95' if (self.total_mileage >= 50000) else 'PETROL_92'


class DieselCarProduce(CarFactory):
    def __init__(self, gas_tank=60):
        super(DieselCarProduce, self).__init__()
        self.mileage_before_repair = 150000
        self.fuel_consumption = 6
        self.gas_tank = gas_tank
        self.reduce_price = 10.5
        self.fuel = 'DIESEL'

        # def info(self):
        #     print('DIESEL', self.__dict__)


cars = []

for i in xrange(0, TOTAL_CARS_COUNT):
    gas_tank = 75 if CarFactory.car_id % 5 == 0 else 60
    if CarFactory.car_id % 3 == 0:
        cars.append(DieselCarProduce(gas_tank))
    else:
        cars.append(PetrolCarProduce(gas_tank))

gallons = []

for i in xrange(0, TOTAL_CARS_COUNT):
    gallons.append(cars[i].mileage_to_drive / (cars[i].fuel_consumption * cars[i].gas_tank))
    cars[i].gas_gallons = gallons[i]

total_credit_to_pay = 0
for i in xrange(0, len(cars)):
    remain_before_repair = cars[i].mileage_before_repair

    if isinstance(cars[i], PetrolCarProduce):
        repair_cost = CarServicePrice.PETROL_REPAIR_COST
    elif isinstance(cars[i], DieselCarProduce):
        repair_cost = CarServicePrice.DIESEL_REPAIR_COST
    else:
        repair_cost = 0

    for j in xrange(0, cars[i].mileage_to_drive, CHECK_DISTANCE):
        remain_to_drive = cars[i].mileage_to_drive - cars[i].total_mileage

        DISTANCE = CHECK_DISTANCE if (remain_to_drive >= CHECK_DISTANCE) else remain_to_drive

        if isinstance(cars[i], PetrolCarProduce):
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
            cars[i].start_price -= CarServicePrice.ENGINE_REPLACE
            cars[i].total_credit += cars[i].start_price
            break

        cars[i].mileage_increase(DISTANCE)
        cars[i].total_fuel += (DISTANCE * cars[i].fuel_consumption / 100)
        cars[i].start_price -= (
        (cars[i].fuel_consumption * FuelPrice.__dict__[cars[i].fuel] * DISTANCE / 100) + cars[i].reduce_price)
        cars[i].fuel_consumption += cars[i].fuel_consumption * FUEL_CONSUMPTION_INCREASE
        #
        if cars[i].start_price <= 0:
            cars[i].total_credit += (cars[i].start_price * (-1) + CarServicePrice.ENGINE_REPLACE)
        total_credit_to_pay += cars[i].total_credit
        cars[i].total_fuel_cost = cars[i].total_fuel * FuelPrice.__dict__[cars[i].fuel]
        cars[i].gas_gallons_used = cars[i].total_fuel / cars[i].gas_tank
        cars[i].mileage_before_util = cars[i].start_price / FuelPrice.__dict__[cars[i].fuel] if (cars[i].start_price >= 0) else 0

for i in xrange(0, TOTAL_CARS_COUNT):
    print("Car's id: {}, total mileage: {}, final price: {}, money spent for fuel: {}, total gas gallons used: {}, "
          "mileage before utilization: {} ".format(cars[i].car_id, cars[i].total_mileage, cars[i].start_price,
                                                   cars[i].total_fuel_cost, cars[i].gas_gallons_used,
                                                   cars[i].mileage_before_util))
    # print(cars[i].__dict__, "fuel price: " + str(FuelPrice.__dict__[cars[i].fuel]))

print('Total credit to pay = ' + str(total_credit_to_pay))

# car1 = CarProduce()
#
# car1.info()
