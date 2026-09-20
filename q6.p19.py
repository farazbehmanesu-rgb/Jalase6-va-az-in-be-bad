sabad = []
products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]


code = input("code mahsol ro vared kon")
for i in products:
    if i ["code"] == code:
        print ( i ["code"], 'name:',i ["name"], 'price :',i ["price"],"mojodi :",i ["stock"])
        sabad_kharid = input("aya be sabed khared ezafe beshe?(bale / kheir)")
        if sabad_kharid == 'bale' and i ["stock"] > 0:
            sabad.append(i)
            i['stock'] -=1
            print(sabad)
            print ('name:',i ["name"],"mojodi :",i ["stock"])
            break


        elif sabad_kharid == 'bale' and i ["stock"] == 0:
                    print("mojod nist")
                    break
else:
    print("none")    