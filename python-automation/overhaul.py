import eugene_filippovich_p7


def overhaul():
    gas_gallons = (cars[0].__dict__['mileage_to_drive'] / (cars[0].__dict__['fuel_consumption']
                   * cars[0].__dict__['gas_tank']))

    print("{} gallons are needed".format(gas_gallons))