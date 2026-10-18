etlaat = []
while True:
    try:
        esm = input ("esmeto vard kon vagti tamom shod bego tamam")
        if esm == "tamam":
            break
        if esm.isdigit():
            raise ValueError("esm nemitone adad bashe")
        
            
        nomre = int(input("nomre ro vared kon"))
        if not 0 <= nomre <= 20:
            raise ValueError("nomre nemitone bishtar az 20 ya kam tar az 0 bash")

    except ValueError :  #SyntaxError: expected 'except' or 'finally' block
        print("yek eshtebah anjam shode")
        continue
    for i in etlaat:
        if i[0] == esm:
            i[1] = nomre
            print("nomre update shod")
            break
    else:      
        etlaat.append ([esm , nomre])

with open("nomarat.txt" , "w") as file:
        file.write(str(etlaat))

with open ("nomarat.txt" , "r") as file:
        print (file.read())

def miangin (etlaat):
    shro = 0
    for i in etlaat:
        shro += int(i[1])
    return shro / len (etlaat)
print("miangin:", miangin(etlaat))
bartar = input("nomre bartar ro namaiesh bedam? (yes , no)")
if bartar == "yes":
     had_agal=int(input("had agal nomre ro vared kon"))
     for i in etlaat:
          if int(i[1]) >= had_agal:
               print(i[0],i[1])
elif bartar == "no":
     print("amaliat anjam shod")
else:
     raise ValueError ("bayad yes ya no bezani")