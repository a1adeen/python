def CARG(pv , fv , n):
    return ((fv / pv)**(1 / n) - 1) * 100


cr = CARG(23299 , 43798 , 5)
print(cr)