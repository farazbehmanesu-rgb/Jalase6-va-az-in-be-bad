def kar_name (nomre):
    if nomre > 100 :
        print ("eshtebah vared kardi")
        return kar_name
    elif nomre >90 :
        print("a")
        return kar_name
    elif nomre >80 :
            print("b")
            return kar_name
    elif nomre >70 :
            print("c")
            return kar_name
    elif nomre >60 :
            print("d")
            return kar_name
    elif nomre <60 :
            print("f")
            return kar_name
print(kar_name(67))