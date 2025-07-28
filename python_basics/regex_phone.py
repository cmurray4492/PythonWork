import re

text = "Please contact me at 713-456-7890 or via email at john@example.com or at cmurray4492@gmail.com"

pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"

matches = re.findall(pattern, text)
# print(pattern)
# print(text)
print(matches)
