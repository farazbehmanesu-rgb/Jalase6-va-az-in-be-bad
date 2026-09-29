employees = {
    "E01": {"name": "Ali", "age": 28, "salary": 3000},
    "E02": {"name": "Sara", "age": 32, "salary": 4500},
    "E03": {"name": "Reza", "age": 25, "salary": 2800}
}
adad2 = 100000000000
kam = {}
adad = 0
bishtarin ={}
soal = int(input("adad ra vared kon ta hoqoq hay bishtar ro behet begam"))
for i in employees:
    if employees[i]["salary"] > adad:
        adad = employees[i]["salary"]
        bishtarin = employees[i]
    
    if employees[i]["salary"] < adad2:
            adad2 = employees[i]["salary"]
            kam = employees[i]

    while soal < employees[i]["salary"]:
         print (employees[i]["name"])
         break
print ("bishtarin hoqoq ro in fard migire :" ,bishtarin["name"])
print ("kam tarin hoqoq ro in fard migire:",kam["name"])
