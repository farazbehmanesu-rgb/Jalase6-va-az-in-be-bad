
import os
import math
jam = 0 
py = 0
text = 0
bozorg_tarin = 0
kochik_tarin = 100000000000000000000000000000000
masir = input("masir ra vared konid")
file_ha = os.listdir(masir)

for i in file_ha:
    hajm = os.path.getsize(masir + "/" + i)
    jam = jam + hajm
    print("poshe ha:")
    print(i, "size",(math.ceil (hajm)))

    if hajm > bozorg_tarin:
        bozorg_tarin = hajm
        bozorg = i

    if hajm < kochik_tarin:
        kochik_tarin = hajm
        kochik = i

    if i.endswith(".py"):
        py += 1

    elif i.endswith(".txt"):
        text =+ 1
        

print("tdad:", len(file_ha))
print("majmo:", jam)
print("miangin:", jam / len(file_ha))
print("bozorg tarin:", bozorg, bozorg_tarin)
print("kochik tarin:", kochik, kochik_tarin)
print ("tedad file hai .py :", py)
print ("tedad file hai .text",text)
