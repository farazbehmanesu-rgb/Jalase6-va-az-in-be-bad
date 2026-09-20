movies = [
    {
        "name": "Inception",
        "genre": "action",
        "age": 13,
        "score": 8.8
    },
    {
        "name": "Titanic",
        "genre": "romance",
        "age": 12,
        "score": 7.9
    },
    {
        "name": "The Conjuring",
        "genre": "horror",
        "age": 16,
        "score": 7.5
    },
    {
        "name": "Interstellar",
        "genre": "science fiction",
        "age": 10,
        "score": 8.7
    },
    {
        "name": "John Wick",
        "genre": "action",
        "age": 18,
        "score": 8.0
    }
]
sen = int(input("sento vared kon"))
janr = input("jhanr mord alagat rovard kon")
emtiaz = int(input("had agal emtiaz mored nazaret ro vared kon"))
for i in movies:
    if sen >= 18:
        print ("esm film:",i["name"],"|jhanr film:",i["genre"],"|sen mojaz:",i["age"],"|nomre film",i["score"])

    elif sen < 18 and i["genre"]==janr and emtiaz <= i["score"]:
            print ("esm film:",i["name"],"|jhanr film:",i["genre"],"|sen mojaz:",i["age"],"|nomre film",i["score"])

            
        
