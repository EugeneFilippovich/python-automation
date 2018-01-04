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
        print (self.wheels, self.spare, self.color)


black_car = Car()
red_car = Car(spare=0, color="Red")

# black_car.diag()
# red_car.diag()

print(black_car.id, black_car.wheels, black_car.spare, black_car.color)
print(red_car.id, red_car.wheels, red_car.spare, red_car.color)


