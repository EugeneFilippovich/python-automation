<<<<<<< HEAD
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

=======
class Car:
    driving_wheels = 4
    spare_wheels = 1
    color = "Black"

    def __init__(self, driving_wheels, spare_wheels, color):
        self.driving_wheels = driving_wheels
        self.spare_wheels = spare_wheels
        self.color = color

    def diag(self):
        print (self.driving_wheels, self.spare_wheels, self.color)



# class RedCar (Car):
#     red_car = Car(4, 0, "Red")
#     print (red_car.driving_wheels, red_car.spare_wheels, red_car.color)


car1 = Car(4, 0, "Red")
car2 = Car(4, 45, 56)
car3 = Car(4, 45, 56)

car1.diag()
car2.diag()
car3.diag()
>>>>>>> origin/master
