# regular expression
import re

pattern = r"[A-Z]inks"
text = '''The open Web presents incredible opportunities for developers. To take full advantage of these 
technologies, you need to know how to use them. Below you'll find  Minks Links to our Web technology documentation.'''


sarch = re.findall(pattern , text)
for s in sarch:
    print(s)