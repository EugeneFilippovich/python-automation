class CarProduce(object):
    car_id = 1

    def __init__(self):
        print("Creating new car {}".format(id(self)))
        self.car_id = CarProduce.car_id
        CarProduce.car_id += 1
        self.start_price = 10000
        self.gas_tank = 60



class Petrol(CarProduce):
    def __init__(self):
        super(Petrol, self).__init__()
        self.petrol_price = 2.4
        self.mileage_before_repair = 100000
        self.repair_cost = 500
        self.fuel_consumption = 8


class Diesel(CarProduce):
    def __init__(self):
        super(Diesel, self).__init__()
        self.diesel_price = 1.8
        self.mileage_before_repair = 150000
        self.repair_cost = 750
        self.fuel_consumption = 6

[Petrol() for x in xrange(1, 100,2)]

#
#
#

# range()


# [Petrol() for x in xrange(1, 100, 10)]



# car1 = Diesel()

# print(car1.__dict__)


