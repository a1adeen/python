# word_replacment programme

# function to replace the required word


n = input('enter the strinig here :')

def repl(n):


    word_to_replace = input('enter the word to replace :')
    word_for_replacemet = input('enter the word for replacement :')
    return n.replace(word_to_replace , word_for_replacemet)


hey = repl('hey my name is ishant')
print(hey)







































def name(nam):
    word_to_replace = input('enter the word u want to replace :')
    word_for_reoplacement = input('enter the replacement word :')
    return nam.replace(word_to_replace , word_for_reoplacement)



hey = name('aur bhai kesa hai tera name kya hai')
print(hey)