import re

text = "date: 2023-06-08"

pattern = r"\d{4}-\d{2}-\d{2}"

dates  = re.findall(pattern, text)

print(dates)


text2 = "date: 2023-6-8"

pattern = r"\d{4}-\d{1,2}-\d{1,2}"

dates  = re.findall(pattern, text2)

print(dates)