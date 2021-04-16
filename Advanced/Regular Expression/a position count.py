#when we will get 3 a...at what postion

import re

x="a{3}"
r = "aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())