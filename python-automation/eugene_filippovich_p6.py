class Car:
    driving_wheels = 4
    spare_wheels = 1
    total_wheels = 5
    color = "Black"

    def __init__(self, driving_wheels, spare_wheels, total_wheels, color):
        self.driving_wheels = driving_wheels
        self.spare_wheels = spare_wheels
        self.total_wheels = total_wheels
        self.color = color

    def diag(self):
        print (Car.driving_wheels, Car.spare_wheels, Car.total_wheels, Car.color)





class RedCar (Car):
    red_car = Car(driving_wheels=4, spare_wheels=0, total_wheels=4, color="Red")
    print (red_car.driving_wheels, red_car.spare_wheels, red_car.total_wheels, red_car.color)


