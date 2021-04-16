import re

x='[a]b$'
r = "aaab abc aaaa cgab"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())