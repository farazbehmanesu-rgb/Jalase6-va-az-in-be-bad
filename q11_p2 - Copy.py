
import math

# Class Product

class Product:
    def __init__(self, code, name, price, stock, sell_count):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        self.sell_count = sell_count

    def show(self):
        print("Code:", self.code)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)
        print("Sell Count:", self.sell_count)

    def sell(self, quantity):
        if quantity > 0 and quantity <= self.stock:
            self.stock -= quantity
            self.sell_count += quantity
            print("Forosh ba movafaghiat anjam shod")
        else:
            print("Mojoodi kafi nist")

    def restock(self, quantity):
        self.stock += quantity
        print("Mojoodi ezafe shod")

    def apply_discount(self, percentage):
        if percentage > 0 and percentage <= 100:
            new_price = self.price * (1 - percentage / 100)
            print("Gheymat jadid:", new_price)
        else:
            print("kod eshtebah ast")

    def is_available(self, nam_mahsol):
        if nam_mahsol in self.name:
            print(self.name, self.stock)
        else:
            print("mojod nist")


# Class Location

class Location:
    def __init__(self, address, x, y):
        self.address = address
        self.x = x
        self.y = y

    def calculate_distance(self, other_location):
        distance = math.sqrt(
            (self.x - other_location.x)**2 +
            (self.y - other_location.y)**2
        )
        return distance


# Class DigitalProduct

class DigitalProduct(Product):
    def __init__(self, code, name, price, stock, sell_count, download_link):
        super().__init__(code, name, price, stock, sell_count)
        self.download_link = download_link

    def get_download_link(self):
        return self.download_link


# Class PhysicalProduct

class PhysicalProduct(Product):
    def __init__(self, code, name, price, stock, sell_count, weight, warehouse_location):
        super().__init__(code, name, price, stock, sell_count)
        self.weight = weight
        self.warehouse_location = warehouse_location

    def calculate_shipping(self, destination):
        distance = self.warehouse_location.calculate_distance(destination)
        return distance * self.weight * 1000


# Sakht Location

location1 = Location("Tehran", 3, 4)
location2 = Location("Shiraz", 6, 8)


# Sakht Digital Products

digital1 = DigitalProduct(101, "Python", 500000, 10, 0, "python.com")
digital2 = DigitalProduct(102, "Photoshop", 700000, 15, 0, "photoshop.com")


# Sakht Physical Products

physical1 = PhysicalProduct(103, "Laptop", 50000000, 5, 0, 2, location1)
physical2 = PhysicalProduct(104, "Mobile", 20000000, 8, 0, 1, location2)


# Namayesh Digital Products

print("\n--- Digital Products ---")

digital1.show()
print("Download Link:", digital1.get_download_link())

print("----------------")

digital2.show()
print("Download Link:", digital2.get_download_link())


# Namayesh Physical Products

print("\n--- Physical Products ---")

physical1.show()
print("Weight:", physical1.weight)

print("----------------")

physical2.show()
print("Weight:", physical2.weight)


# Test Forosh

print("\n--- Sell ---")

digital1.sell(2)
physical1.sell(1)


# Test Ezafe kardan Mojoodi

print("\n--- Restock ---")

digital2.restock(5)
physical2.restock(3)


# Test Takhfif

print("\n--- Discount ---")

digital1.apply_discount(20)
physical1.apply_discount(10)


# Test Fasele

print("\n--- Distance ---")

print("Distance:", location1.calculate_distance(location2))


# Test Hazine Ersal

print("\n--- Shipping Cost ---")

print("Laptop Shipping:", physical1.calculate_shipping(location2))

print("Mobile Shipping:", physical2.calculate_shipping(location1))


# Namayesh Mojoodi Nahayi

print("\n--- Final Stock ---")

digital1.show()
digital2.show()
physical1.show()
physical2.show()
