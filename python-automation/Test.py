class Car(object):
    VIN = 42

    def __init__(self, color="Black"):
        print("Creating new car {}".format(id(self)))
        self.vin = Car.VIN
        self.color = color
        self.fuel = 42
        self.distance = 0
        Car.VIN += 1

    def fill_tank(self, count=42):
        self.fuel = count
        # me.money -= count



        # self.vin = 42

    def drive(self, distance=0):
        self.distance += distance
        self.fuel -= 5
        print("Driving car")


mazda = Car()
print(mazda.vin)
print(mazda.__dict__['vin'])
print(id(mazda))

mazda.drive()
Car.drive(mazda)
print(mazda.__dict__)
opel = Car()
print(opel.__dict__)


test = Car()
print(test.__dict__)

print(Car.VIN)











































