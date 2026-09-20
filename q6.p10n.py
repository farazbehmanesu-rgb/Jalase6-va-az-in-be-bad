nomarat = input("nomre khodeto vared kon")
jam = 0
while True:
    nomre = int(input ("nomarat ra vared konid va vagti tamom shod 000 bezan"))
    if nomre == 000:
        for i in nomarat:
            jam += i 
        tedad = len(nomarat)
        print (jam / tedad )
        break
    elif nomre < 21:
        nomarat.append(nomre)
        
        print(nomarat)
    