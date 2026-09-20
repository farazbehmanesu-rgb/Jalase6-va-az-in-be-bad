import random

a = (random.randint(1,100))

while True:
    hads = int(input("be nazaret adad chande"))
    if a > hads:
        print("eshtebah adad (bishtar) az ine dobare bezan")

    elif a < hads:
        print("eshtebah adad (kam tar) az ine dobare bezan")

    elif a == hads:
        print ("afarin")
        break