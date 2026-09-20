user1 = input("entekhab kon (sang/kaqaz/gheichi)")
print ("hala bede nafar bad e bezane va entekhab kone" )
enter = input("e bezan")
if enter == "e":
    user2 = input("entekhab kon (sang/kaqaz/gheichi)")
    if user1 == "sang" and user2 == "gheichi":
        print ("user 1 bord")
    elif user1 == "kaqaz" and user2 == "gheichi":
        print("user 2 bord")
