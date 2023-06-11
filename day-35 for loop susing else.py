# for loop with else

for i in range(5):
    print(i)


else:
    print("hey there")


# condition
# if we run a loop and its range is 6 and it breaksat 4 then the esle statement will be printed ?
for h in range(6):
    print(h)
    if h == 4:
        break

else:
        print("it ends")

# answer is yes    


# in while loop 

# hey = int(input())
# while hey   <= 9 :
#      print(i)
#      i = i +1
# else:
#      print("it ends here")     



for j in range(8):
     print(f"itration no. {j} is in loop ")


else:
     print("else block in loop ")     
     print("out of loop")