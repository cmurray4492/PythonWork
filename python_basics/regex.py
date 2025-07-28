import re
string = "abca"
pattern = "a"

if re.search(pattern, string):
    print('Match Found')
else:
    print("No match found")
