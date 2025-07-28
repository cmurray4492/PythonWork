import re

text = "Please contact me at 713-456-7890 or via email at john@example.org or at cmurray4492@gmail.com"

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

matches = re.findall(pattern, text)
# print(pattern)
# print(text)
print(matches)
