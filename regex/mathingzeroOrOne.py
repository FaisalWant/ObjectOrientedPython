#mathingzeroOrOne.py
import re
randStr= "doctor doctors doctor's"
regex= re.compile("[doctor]+['s]*")
matches= re.findall(regex,randStr)
for i in matches:
	print(i)