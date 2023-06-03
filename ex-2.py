# programme that says gm , good afternoon and  good night according to time zone
import time


samay = time.strptime('%H:%M:%S')
hours = int(time.strftime('%H'))
print(samay)


# if conditions
if (samay>0  & samay<12):
    print("goood morning")
elif(samay > 12 & samay > 18 ):
    print('good afternoon')
    if(samay > 18 & samay <20):
        print("good evenuing")
    else:
        print("good night")
    