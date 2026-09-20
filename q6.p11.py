gabol = []
mardod = []
while True:
    nomre = int(input ("nomarat ra vared konid va vagti tamom shod 000 bezan"))
    if nomre == 000 :
        print ("tedad kasani ke gabol shidand " , teded )
        print("kasani ke gabol shodand",gabol)
        print ("kasanik mardod shodadnd " , mardod)
        break
    elif nomre > 21 :
        print ("bishtar az 20 nemitoni vared koni ")
    elif nomre >= 10 :
        gabol.append(nomre)
        teded = len (gabol) 
        print ("tedad kasani ke gabol shidand " , teded )
        print(gabol)
    elif nomre < 10 :
        mardod.append(nomre)
        print (mardod)

