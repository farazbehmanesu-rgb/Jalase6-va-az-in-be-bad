"""
kalame = str(input("kalame vared kon"))
horof = input ("harf vared kon")
tedad = 0
for i in kalame:
    if i == horof:
        tedad = tedad + 1
print (tedad)
"""




kalame = str(input("kalame vared kon"))
horof = input ("harf vared kon")
tedad = kalame.count(horof)
print (tedad)
