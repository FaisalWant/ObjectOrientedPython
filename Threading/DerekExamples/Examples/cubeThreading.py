import re
# randStr= "<name> Hello my name is faisal afzal </name><name>he is a very evil person</name>"

randStr= "ape at the apex"


regex= re.compile(r"\bape\b")
matches= re.findall(regex, randStr)
print(len(matches))
for i in matches:
	print(i)