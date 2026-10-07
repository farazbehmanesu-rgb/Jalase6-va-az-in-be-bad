def profile_create ():
    vorodi = {}
    vorodi_shahr = {}
    name = input("esm khodn ro vared kon")
    age = input("sen khodn ro vared kon")
    ezafe = input ("agar chiz dige bara neveshtan dari bezan kwargs")
    print ("esm shoma:",name ,"||", "sen shoma:",age)
    if ezafe == "kwargs":
        while True:
            a = input("titel ro vared kon va harvagt tamom shod benvis end")
            if a == "end":
                print ("esm shoma:",name ,"||", "sen shoma:",age)
                print(vorodi)
                print ("tedad vorodi ezafe:",len(vorodi))
                print ("shahr shoma:",vorodi_shahr)
                if "email" not in vorodi:
                    print("email not provided")
                break
            b = input("harchi mikahi benvis")
            if a == "city":
                vorodi_shahr[a]=b
                print (vorodi_shahr)
                continue
            

            
            vorodi[a]=b
            print(vorodi)
            print ("tedad vorodi ezafe:",len(vorodi))

        
        


profile_create()