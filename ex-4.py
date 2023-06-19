# secret code language


st = (input("enter the string here :"))
words = st.split("  ")
coding = False
if(coding):
    nwords = []
    for word in words:
     if(len(word)>= 3):
        strt_1 = "hmk"
        strt_2 =  "njk"
        st_new =  strt_1 + word[1:] + word[0] + strt_2
        nwords.append(st_new)
        
     else:
        nwords.append(word[:: -1])
    print("".join(nwords))

else:
   nwords = []
   for word in words:
       if(len(word)>= 3):
        st_new = word [ 3: -3]
        st_new =   st_new[-1] + st_new[: -1]
        nwords.append(st_new)
       else:
        nwords.append(word[:: -1])
       print("".join(nwords))




# yeyeyeyeyeyeeyeyey did it 