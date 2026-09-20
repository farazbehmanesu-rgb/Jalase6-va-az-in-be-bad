accounts = [
    {
        "username": "ali",
        "password": "1234",
        "balance": 5000,
        "transactions": []
    },
    {
        "username": "sara",
        "password": "5678",
        "balance": 8000,
        "transactions": []
    }
]

esm = input("username khod ra vared konid: ")

for i in accounts:

    if i["username"] == esm:

        ramz = input("password khod ra vared konid: ")

        if i["password"] == ramz:

            print("shoma vareed shodid")

            a = input("chikar mikoni (bardasht/entegal/change): ")

            if a == "bardasht":

                pol = int(input("mablagh mored nazar ra bardasht kon: "))

                i["balance"] -= pol
                i["transactions"].append(pol)

                print(i["balance"])
                print("tarakonesh hay shoma:", i["transactions"])

            elif a == "entegal":

                esm_shaks = input("esm kasi ke be hesabesh variz mikoni ro vared kon: ")

                mablag = int(input("mablagi ke mikhai variz koni ro bego: "))

                i["balance"] -= mablag

                for a in accounts:

                    if a["username"] == esm_shaks:

                        a["balance"] += mablag

                        print("balance shoma:", i["balance"])
                        print("balance", esm_shaks, ":", a["balance"])
            elif a == "change":
                vahed_pol = input("vahed pol khod ra vared konid(rial/dolar)")
                if vahed_pol == "rial":
                    rial = i["balance"] * 250000
                    print(rial)
                elif vahed_pol == "dolar":
                    print (i["balance"])

            break

else:
    print("none")