ramz = "1234"
talash = 0

while talash < 3:
    vorodi = input("ramz ra vared kon: ")
    talash = talash + 1

    if vorodi == ramz:
        print("vorood movafagh")
        break
    else:
        print("ramz eshtebah ast")

if talash == 3 and vorodi != ramz:
    print("hesab shoma masdood shod")