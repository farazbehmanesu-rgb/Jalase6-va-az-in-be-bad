n = int(input("adad vared kon"))
def numbers_even ():
    for i in range (1,n):
        if i % 2 == 0:
            yield i
a = numbers_even()
print(next(a))
print(next(a))
print(next(a))
         