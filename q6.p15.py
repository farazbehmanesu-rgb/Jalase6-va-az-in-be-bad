
products= {'airpods':0,
           'macbook':2,
           "iphone":5}
nam_mahsol = input("nam mahsol ra vared kon")
if nam_mahsol in products:
    if products[nam_mahsol] > 0:      #>>>ba komak hosh masnoei<<<
        print ("mojod")
    elif products[nam_mahsol] == 0:    
        print ("na mojod")
else:
    print ("mahsol vohjod nadard")
