def sen_mojaz (sen):
    if sen < 18:
        print ("access denied")
        return sen_mojaz
    else:
        print("welcome")
        return sen_mojaz
print(sen_mojaz(5))