products = [
    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
    {'code': 'z2', 'name': 'zara shooes 100', 'price': 45},
    {'code': 'z3', 'name': 'zara cloth 451', 'price': 35},
    {'code': 'z4', 'name': 'zara shooes 300', 'price': 55},
    {'code': 'z5', 'name': 'zara shooes 231', 'price': 60},
    {'code': 'z6', 'name': 'zara bag 400', 'price': 110},
    {'code': 'z7', 'name': 'zara bag 500', 'price': 95}
]
vorodi = input("kod mahsol ro vared kon")
for i in products:
    if i['code'] == vorodi:
        print ("kod mahsol:",i["code"],'||',"esm mahsol:",i["name"],'||',"geimat mahsol:",i['price'])