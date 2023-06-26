# practise
with open("next.txt",'r') as f:
    f.seek(4)
    data = f.read(6)
    print(data)



with open('hey.txt','r') as nise:
    hey = nise.read()
    nise.close()
    print(hey)