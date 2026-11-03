
class customer:
    def __init__(self, esm, price, quantity, category):
        self.esm = esm
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_price(self):
        ghaymat = int(input("gheymat ra vared konid: "))
        self.price = ghaymat

    def add_stock(self):
        mojodi = int(input("tedad mojodi jadid ra vared konid: "))
        if mojodi >= 0:
            self.quantity = mojodi
        else:
            print("mojodi nemitavanad manfi bashad")

    def sell(self):
        nam = input("nam mahsol ra vared konid: ")

        if nam == self.esm:
            if self.quantity > 0:
                self.quantity = self.quantity - 1
                print("mojodi baghimande:", self.quantity)
            else:
                print("mojod nist")
        else:
            print("mahsol yaft nashod")

    def __str__(self):
        return self.esm + "|||" + str(self.price)

    def apply_discount(self):
        takhfif = input("kod takhfif khod ra vared konid: ")
        if takhfif == "12340":
            self.price = self.price * 0.8
            print("gheymat ba takhfif:", self.price)
        else:
            print("kod takhfif eshtebah ast")

    def total_value(self):
        majmo = input("nam mahsol ra vared konid: ")
        if majmo == self.esm:
            a = self.price * self.quantity
            print("arzesh kol mojodi:", a)
        else:
            print("mahsol yaft nashod")


obj = customer("kiko", 100000, 100, "araiesh")

print("1. namayesh mahsol")
print("2. taghir gheymat")
print("3. ezafe kardan mojodi")
print("4. foroosh ")
print("5. takhfif")
print("6. arzesh kol mojodi")

entekhab = input("yek gozine entekhab konid: ")

if entekhab == "1":
    print(obj)
    print("mojodi:", obj.quantity)
    print("daste bandi:", obj.category)

elif entekhab == "2":
    obj.update_price()
    print(obj)

elif entekhab == "3":
    obj.add_stock()
    print("mojodi:", obj.quantity)

elif entekhab == "4":
    obj.sell()

elif entekhab == "5":
    obj.apply_discount()
    print(obj)

elif entekhab == "6":
    obj.total_value()

else:
    print("gozine eshtebah ast")

