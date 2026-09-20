pas = input("pasvord vared kon")
sabad = 0
if len (pas) < 8 :
    print("bayad bish az 8 ragam bashe")
    exit()
for i in pas:
    if i.isalpha():
        sabad = sabad +1
        break

for i in pas:
    if i.isdigit():
        sabad = sabad +2
        break
if sabad == 2 :
    print ("horof vared kon")
if sabad == 1 :
    print ("adad vared kon")
if sabad == 3 :
    print ("sabt shod")
    