def add_user():
    while True:
        esm = input("Nam ra vared kon ya e bezan: ")

        if esm == "e":
            break

        with open("users.txt", "r") as file:
            esm_ha = file.readlines()

        for i in esm_ha:
            if esm in i:
                print("Esme tekrari ast")
                break
        else:
            gmail = input("Gmail ra vared kon: ")

            with open("users.txt", "r") as file:
                gmail_ha = file.readlines()

            for i in gmail_ha:
                if gmail in i:
                    print("gmail tekrari ast")
                    break
            else:
                vazeyat = input("active or blocked: ")
                if vazeyat != "active" and vazeyat != "blocked":
                    print("Bayad yeki ra entekhab koni")
                    continue

                with open("users.txt", "a") as file:
                    file.write(esm + " " + gmail + " " + vazeyat + "\n")

                print("User zakhire shod")
                continue

            continue

        continue
def find_user(esm):
    with open("users.txt", "r") as file:
        for i in file:
            if esm in i:
                print(i)
                return

    print("User peyda nashod")
def deleta_user (esm):
    with open ("users.txt", "r") as file:
        esm_ha = file.readlines()
    with open ("users.txt", "w") as file:
        for i in esm_ha:
            if esm not in i:
                file.write(i)
            else :
                print("user hazf shod")
def updat_user(esm):
    soal = input("Mikhai ke gmail ya vazeyat karbar ro taghir bedi? (yes / no): ")

    if soal == "yes":
        esm = input("Nam ra vared kon: ")

        with open("users.txt", "r") as file:
            esm_ha = file.readlines()

        for i in esm_ha:
            if esm in i:
                gmail = input("Gmail ra vared kon: ")
                vazeyat = input("active or blocked: ")

                esm_ha.remove(i)
                esm_ha.append(esm + " " + gmail + " " + vazeyat + "\n")
                break

        with open("users.txt", "w") as file:
            file.writelines(esm_ha)
    elif soal == "no":
        print ("dariaft shod")
        return 
    else :
        print ("eshtebah vared kardi")
def list_users():
    with open ("users.txt", "r") as file:
        print (file.readlines())
def generation_report(vazeyat):  
    with open ("users.txt",'r') as file:
        vazeyat_ha = file.readlines()
        activha = 0
        for i in vazeyat_ha:
            if vazeyat == "active":
                if "active" in i :
                    activha += 1
        print (activha)            
                
open("users.txt", "a").close()
while True:
    soal = input("1: Add user, 2: Find user, 3: Exit, 4: Delete user, 5: Update user, 6: List users, 7: Generation report ,exit : khoroj")

       

    if soal == "1":
        add_user()

    elif soal == "2":
        esm = input("Nam user ra vared kon: ")
        find_user(esm)

    elif soal == "3":
        print ("az barname kharej shodid")
        break

    elif soal == "4":
        esm = input("Nam user ra vared kon: ")
        deleta_user(esm)

    elif soal == "5":
        esm = input("Nam user ra vared kon: ")
        updat_user(esm)

    elif soal == "6":
        list_users()

    elif soal == "7":
        vazeyat = input("Vazeyat ra vared kon (active): ")
        generation_report(vazeyat)

    else:
        print("Entekhab eshtebah ast")