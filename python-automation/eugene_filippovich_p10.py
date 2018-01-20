from operator import attrgetter


class Bouquet(object):
    def __init__(self):
        self.flower_bouquet = []
        self.total_price = 0
        self.average_life_time = 0.0

    def __getitem__(self, price):
        return getattr(self, price)

    def add_flowers(self, *flowers):
            for flower in flowers:
                if flower.is_broken == False:
                    self.flower_bouquet.append(flower)

    # def sorting_by_key(self):
    #     bouquet.flower_bouquet.sort(key=attrgetter('price'), reverse=True)

    def get_average_life_time(self):
        for flower in self.flower_bouquet:
            self.average_life_time += flower.life_time
        return self.average_life_time / len(self.flower_bouquet)

    def get_total_price(self):
        for flower in self.flower_bouquet:
            self.total_price += flower.price
        return self.total_price

    def destruct_bouquet(self):
        for flower in self.flower_bouquet:
            flower.is_broken = True
        self.flower_bouquet = []

    def check_contains(self, flower):
        return flower in self.flower_bouquet


class Flower(object):

    def __init__(self, color, length, price, life_time):
        self.color = color
        self.length = length
        self.price = price
        self.life_time = life_time
        self.is_broken = False


class Roses(Flower):
    def __init__(self, color, length, price, life_time):
        self.name = "Rose"
        Flower.__init__(self, color, length, price, life_time)


class Tulips(Flower):
    def __init__(self, color, length, price, life_time):
        self.name = 'Tulip'
        Flower.__init__(self, color, length, price, life_time)


class Peonies(Flower):
    def __init__(self, color, length, price, life_time):
        self.name = 'Pion'
        Flower.__init__(self, color, length, price, life_time)

bouquet = Bouquet()
r = Roses('Red', 40, 5, 3)
t = Tulips('White', 50, 4, 4)
p = Peonies('Purple', 30, 2, 3)
bouquet.add_flowers(r, t, p)
print(bouquet.get_total_price())
print(bouquet.get_average_life_time())

bouquet.destruct_bouquet()

print(bouquet.check_contains(p))

b2 = Bouquet()
p2 = Peonies('Purple', 30, 2, 3)
b2.add_flowers(r, p2)
# bouquet.sorting_by_key()
# print(bouquet.life_time)

for i in bouquet.flower_bouquet:
    print i.__dict__

print ('____________')

for i in b2.flower_bouquet:
    print i.__dict__
