
class Vehicle:
    def __init__(self, brand, model, year, distance_traveled):
        self.brand = brand
        self.model = model
        self.year = year
        self.distance_traveled = distance_traveled

    def show_info(self):
        print("\n--- Vehicle Information ---")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Distance:", self.distance_traveled)

    def drive(self, distance_traveled):
        if distance_traveled > self.distance_traveled:
            self.distance_traveled = distance_traveled
            print("Masafat taghir kard")
        else:
            print("Masafat jadid bayad bishtar bashe")

    def calculate_trip_cost(self, distance):
        raise NotImplementedError


class Car(Vehicle):
    def calculate_trip_cost(self, distance):
        cost = distance * 1000
        return cost


class gascar(Vehicle):
    def __init__(self, brand, model, year, distance_traveled):
        super().__init__(brand, model, year, distance_traveled)

    def fuel_consumption(self, distance, fuel):
        masraf = (fuel / distance) * 100
        print("Masraf benzine dar har 100 km:", masraf)

    def calculate_trip_cost(self, distance):
        masraf = 8
        hazine = (distance / 100) * masraf * 3000
        return hazine


class electruc(Vehicle):
    def __init__(self, brand, model, year, distance_traveled):
        super().__init__(brand, model, year, distance_traveled)

    def energy_consumption(self, distance, electrucp):
        masraf_b = (electrucp / distance) * 100
        print("masraf kilo vat dar har 100 km:", masraf_b)

    def calculate_trip_cost(self, distance):
        masrafb = 15
        hazineb = (distance / 100) * masrafb * 3000
        return hazineb


# Sakht 4 object

car1 = gascar("BMW", "X5", 2022, 15000)

car2 = gascar("Benz", "C200", 2021, 20000)

car3 = gascar("Toyota", "Camry", 2023, 10000)

car4 = electruc("Tesla", "Model 3", 2024, 5000)


# Gharar dadan dar List

vehicles = [car1, car2, car3, car4]


# Ejraye halghe

for vehicle in vehicles:
    vehicle.show_info()
    print("Hazine safar 150 km:")
    print(vehicle.calculate_trip_cost(150))

