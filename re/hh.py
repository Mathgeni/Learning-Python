import re

pattern = r'\d+\d'
text = '3 fsda asdf 200s0'
print(re.findall(pattern, text))
