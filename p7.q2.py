inventory = {"apple":20, "banana":5, "orange":0, "milk":12, "bread":0}
mojod ={}
na_mojod = {}
for i in inventory:
    if inventory[i] > 0:
        a = mojod = inventory[i]
        mojod = i
        print ("mojodi shoma" , mojod , a)


    if inventory[i] <= 0:
            b = na_mojod = inventory[i]
            na_mojod = i
            print ("list na mojodi" ,na_mojod , b)
    
