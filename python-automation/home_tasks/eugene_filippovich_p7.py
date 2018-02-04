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
    car_id = 0
    cars = []

    def __init__(self):
        print("Creating new car {}".format(id(self)))
        self.car_id = CarFactory.car_id
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
        self.total_fuel_cost = 0
        self.gas_gallons_used = 0
        self.mileage_before_util = 0
        CarFactory.car_id += 1

    @property
    def _total_mileage(self):
        return self.total_mileage

    def mileage_increase(self, distance=0):
        if distance > 0:
            self.total_mileage += distance

    def info(self):
        print('mycar')

    def create_cars(self, total_cars_count=100):
        for i in xrange(0, total_cars_count):
            gas_tank = 75 if CarFactory.car_id % 5 == 0 else 60
            if CarFactory.car_id % 3 == 0:
                self.add_car(DieselCarProduce(gas_tank))
            else:
                self.add_car(PetrolCarProduce(gas_tank))

    def add_car(self, car):
        self.cars.append(car)

    def get_statistic(self):
        for car in self.cars:
            car.get_car_stats()

    def get_car_stats(self):
        print("Car's id: {}, total mileage: {}, final price: {}, money spent for fuel: {}, total gas gallons used: {}, "
              "mileage before utilization: {} ".format(self.car_id, self._total_mileage, self.start_price,
                                                       self.total_fuel_cost, self.gas_gallons_used,
                                                       self.mileage_before_util))

    total_credit_to_pay = 0

    def drive_distance(self):
        for car in self.cars:
            remain_before_repair = car.mileage_before_repair

            if isinstance(car, PetrolCarProduce):
                repair_cost = CarServicePrice.PETROL_REPAIR_COST
            elif isinstance(car, DieselCarProduce):
                repair_cost = CarServicePrice.DIESEL_REPAIR_COST
            else:
                repair_cost = 0
            for j in xrange(0, car.mileage_to_drive, CHECK_DISTANCE):
                remain_to_drive = car.mileage_to_drive - car.total_mileage

                DISTANCE = CHECK_DISTANCE if (remain_to_drive >= CHECK_DISTANCE) else remain_to_drive

                if isinstance(car, PetrolCarProduce):
                    car.change_petrol_price()

                if remain_before_repair < DISTANCE:
                    if (car.start_price - repair_cost) <= 0:
                        continue
                    car.start_price -= repair_cost
                    car.repair_count += 1
                    remain_before_repair = car.mileage_before_repair - (DISTANCE - remain_before_repair)
                else:
                    remain_before_repair -= DISTANCE

                if car.start_price <= 0:
                    car.start_price -= CarServicePrice.ENGINE_REPLACE
                    car.total_credit += car.start_price
                    break

                car.mileage_increase(DISTANCE)
                car.total_fuel += (DISTANCE * car.fuel_consumption / 100)
                car.start_price -= (
                    (car.fuel_consumption * FuelPrice.__dict__[car.fuel] * DISTANCE / 100) + car.reduce_price)
                car.fuel_consumption += car.fuel_consumption * FUEL_CONSUMPTION_INCREASE
                if car.start_price <= 0:
                    car.total_credit += (car.start_price * (-1) + CarServicePrice.ENGINE_REPLACE)
                self.total_credit_to_pay += car.total_credit
                car.total_fuel_cost = car.total_fuel * FuelPrice.__dict__[car.fuel]
                car.gas_gallons_used = car.total_fuel / car.gas_tank
                car.mileage_before_util = car.start_price / FuelPrice.__dict__[car.fuel] if (car.start_price >= 0) else 0


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

car_produce = CarFactory()
car_produce.create_cars(TOTAL_CARS_COUNT)

car_produce.drive_distance()

cars = CarFactory.cars

car_produce.get_statistic()

print('Total credit to pay = ' + str(car_produce.total_credit_to_pay))
