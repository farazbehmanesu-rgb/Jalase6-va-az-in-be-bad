products = {"laptop":3
            ,"phone":0
            ,"tablet":5
            ,"mouse":0
            ,"keyboard":2}
def products_available ():
    for i in products:
        if products[i] > 0 :
            yield i
a = products_available()
for i in a:
    print (next(i))