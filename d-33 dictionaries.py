# dictionaries
# example of an dictionary 
dict = {
    "aladden":"player",
    "desk":"object"
}

print(dict["aladden"])
# !in this dictionary aladden is key and player is value 


# to get all the keys from the dictionary 

all_key = {"aladeen" : "player_1", 
           "rasgulla" : "player_2",
           "summer_sin" : "player_3",
 }

print(all_key)
print(all_key.keys())



# for loops in dictionary 
for key in all_key.keys():
  print(f"value of the folllowing {key} is {all_key[key]}")

#   or we can use this

for key, value in all_key.items():
  print(f"value of the folllowing {key} is {value}")