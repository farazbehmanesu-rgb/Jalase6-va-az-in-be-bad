amal = input("Amal ra vared kon: ")

a = int(input("Adad aval: "))
b = int(input("Adad dovom: "))

if amal == "+":
    print(a + b)

if amal == "-":
    print(a - b)

if amal == "*":
    print(a * b)

if amal == "/":
    print(a / b)

if amal != "+" and amal != "-" and amal != "*" and amal != "/":
    print("Eshtebah vared kardi")