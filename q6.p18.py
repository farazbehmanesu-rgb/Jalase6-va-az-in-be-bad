
users = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    }
]
a = input("salam chi mikhai")
if a == "sabt nam":
    username = input("esmeto vared kon")
    age= input("sento vared kon")
    city = input("shahreto vared kon")
    new_user = {
        "username": username,
        "age": age,
        "city": city,
        "active": True
    }
    users.append(new_user)
    print(users)
elif a == "peida kardan":
    porsesh_esm = input("esm ra vared konid")
    for i in users:
        if i ["username"] == porsesh_esm:
            print (i ["username"] , i["age"],i["city"])
        else:
            print("none")

elif a == "dastresi":
    for i in users:
        if i ["age"] > 17:
            users_bala18 = {
                    "username": i["username"],
                    "age": i["age"],
                    "city": i["city"],
                    "active": True
                }
            print(users_bala18)
elif a == "bedon dastresi":
    for i in users:
        if i ["age"] <= 17:
                    users_zir18 = {
                            "username": i["username"],
                            "age": i["age"],
                            "city": i["city"],
                            "active": False
                        }
                    print(users_zir18)

