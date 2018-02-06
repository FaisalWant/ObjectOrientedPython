#wordBoundaries.py

import re
# randStr= "ape at the apex"
# regex= re.compile(r"\bape\b")
# matches= re.findall(regex,randStr)
# print(matches)


# matching the begining of the strig
#***********************************
# randStr= "Match everything .up to @"
# regex= re.compile(r"^.*[^@]")
# matches= re.findall(regex,randStr)
# print(len(matches))
# for i in matches:
# 	print(i)
#*************************************

#matching the end of the string
#*************************************
# randStr= "@ Get this String"
# regex= re.compile(r"[^@\s].*$")
# matches= re.findall(regex,randStr)
# print(len(matches))
# for i in matches:
# 	print(i)
#******************************************

randStr= """Ape is big 
Turtle is slow
Cheetah is fast"""
regex= re.compile(r"(?m)^.*?\s")
matches= re.findall(regex, randStr)
print(len(matches))
for i in matches:
	print(i)