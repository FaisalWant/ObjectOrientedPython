#subexpression.py
import re
randStr="My number is 412-555-1212"
regex=re.compile(r"412-(.*)")
matches= re.findall(regex, randStr)
print(len(matches))
for i in matches:
	print(i)