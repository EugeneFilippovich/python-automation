class Car(object):
    wheels = None
    car_id = 1

    def __init__(self, wheels=4, spare=1, color="Black"):
        print("Creating new car {}".format(id(self)))
        self.id = Car.car_id
        self.wheels = wheels
        self.spare = spare
        self.color = color
        Car.car_id += 1

    def diag(self):
        print (self.id, self.wheels, self.spare, self.color)



black_car = Car()
red_car = Car(spare=0, color="Red")
black_car1 = Car()

black_car.diag()
red_car.diag()
black_car1.diag()

