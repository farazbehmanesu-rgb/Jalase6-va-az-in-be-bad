
class BankAccount:
    def __init__(self, name, mojodi):
        self.name = name
        self.mojodi = mojodi

    def __str__(self):
        return self.name + " ||| " + str(self.mojodi)

    def deposit(self):
        variz = int(input("Mablagh variz: "))
        if variz > 0:
            self.mojodi += variz
        else:
            print("Mablagh motabar nist")

    def withdraw(self):
        bardasht = int(input("Mablagh bardasht: "))
        if 0 < bardasht <= self.mojodi:
            self.mojodi -= bardasht
        else:
            print("Mojodi kafi nist")

    def transfer(self, other, mablagh):
        if 0 < mablagh <= self.mojodi:
            self.mojodi -= mablagh
            other.mojodi += mablagh
        else:
            print("Mablagh motabar nist")

    def get_balance(self):
        print(self.mojodi)


accounts = []

while True:
    esm = input("Esm (tamam baraye payan): ")
    if esm == "tamam":
        break

    pool = int(input("Mojodi: "))
    accounts.append(BankAccount(esm, pool))


while True:
    print("1. Namayesh")
    print("2. Variz")
    print("3. Bardasht")
    print("4. Enteghal")
    print("5. Mojodi")
    print("6. Khoroj")

    entekhab = input("Entekhab: ")

    if entekhab == "6":
        break

    esm = input("Esm hesab: ")

    for a in accounts:
        if a.name == esm:

            if entekhab == "1":
                print(a)

            elif entekhab == "2":
                a.deposit()

            elif entekhab == "3":
                a.withdraw()

            elif entekhab == "4":
                esm2 = input("Esm hesab maghsad: ")
                for b in accounts:
                    if b.name == esm2:
                        mablagh = int(input("Mablagh: "))
                        a.transfer(b, mablagh)

            elif entekhab == "5":
                a.get_balance()
            break
    else:
        print("Account peyda nashod")
