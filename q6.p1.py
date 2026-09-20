"""
def sen(sal_tavalod , no_tarikh = 'milady' ):

 #   ya shamsi ya milady

    if no_tarikh == "shamsi":
        sen = 1405 - sal_tavalod
        return sen
    elif no_tarikh == "milady":
        sen = 2026 - sal_tavalod
        return sen
print(sen(2007 ))


"""
def sen(sal_tavalod):
        
    if sal_tavalod in range (1,1405):
        sen = 1405 - sal_tavalod
        return sen
    else:
        sen = 2026 - sal_tavalod
        return sen
print(sen(1400 ))

