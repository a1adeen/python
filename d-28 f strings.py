# # string formating

# format string
name_location = "hey my name is {} and i'm from {}"
name = (input("your name :"))
location = (input("country name :"))
print(name_location.format(name,location))

# f String
ingame_name = (input("your in game name :"))
fav_game = (input("your fav. game :"))
about_games = (f"hey my ingame name is {ingame_name} and my fav. game is {fav_game}")
print(about_games)


# example
value = (input("insert value in points :"))
txt = (f"your inserted value is {value}")
print (txt)

# to print the curly brakets ass well
#! in this input tag doesn;t work in f string,,,,,  in this we need to give the orignal value to an element
your_name = "nothing will be printed in the terminal form here"
naaam = (f"your name is {{aladeen}}")
print(naaam)