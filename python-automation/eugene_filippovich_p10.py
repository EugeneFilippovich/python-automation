from operator import attrgetter


class Flowers(object):
    flower_bouquet = []
    total_price = 0

    def __init__(self, color='White', length=50, price=5, life_time=5):
        self.color = color
        self.length = length
        self.price = price
        self.life_time = life_time

    def add_flowers(self, *flowers):
            self.flower_bouquet.extend(flowers)

    # def __getitem__(self, price):
    #     return getattr(self, price)

    # def total_price(self):
    #     Flowers.total_price = sum(map(operator.itemgetter('price'), Flowers.flower_bouquet))
    #     # for flower in Flowers.flower_bouquet:
    #     #     Flowers.total_price += Flowers.flower_bouquet
    #     #  sum([item['price'] for item in Flowers.flower_bouquet])


    def life_time(self):
        pass

    def destruct_bouquet(self):
        pass

    def sorting_by_key(self):
        Flowers.flower_bouquet.sort(key=attrgetter('price'), reverse=False)


class Roses(Flowers):
    def __init__(self, color, length, price, life_time):
        self.name = "Rose"
        Flowers.__init__(self, color, length, price, life_time)


class Tulips(Flowers):
    def __init__(self, color, length, price, life_time):
        self.name = 'Tulip'
        Flowers.__init__(self, color, length, price, life_time)


class Peonies(Flowers):
    def __init__(self, color, length, price, life_time):
        self.name = 'Pion'
        Flowers.__init__(self, color, length, price, life_time)

flowers = Flowers()
r = Roses('Red', 40, 5, 3)
t = Tulips('White', 50, 4, 4)
p = Peonies('Purple', 30, 2, 3)
flowers.add_flowers(r, t, p)
flowers.sorting_by_key()

for i in Flowers.flower_bouquet:
    print i.__dict__
