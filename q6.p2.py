def zoj_fard (adad):
    if adad > 0:
        print("positive")
        if adad % 2 == 0 :
            print ("even")
            zoj_fard = True
            return zoj_fard
        elif adad % 2 != 0 :
            print ("odd")
            zoj_fard = False
            return zoj_fard
    elif adad < 0:
        print("negative")
        if adad % 2 == 0 :
            print ("even")
            zoj_fard = True
            return zoj_fard
        elif adad % 2 != 0 :
            print ("odd")
            zoj_fard = False
            return zoj_fard
    elif adad==0:
        print("zero")
        return adad
print(zoj_fard(0))