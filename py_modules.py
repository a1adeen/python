import collections
from collections import Counter
from collections import defaultdict

# tell the repeated elements
my_list = [1,1,1,1,1,1,2,22, 333,33]
print(Counter(my_list))
# to count how many a word comes in a string
words = ("We use ads to keep our content free for you.Please allow ads and let sponsors fund your surfing.Thank you!")
print(Counter(words.split()))


dct = {
    'hey': 9,
    "hey_2" : 1,
}
print(list(dct))