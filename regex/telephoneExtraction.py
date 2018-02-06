#telephoneExtraction.py
import re
# randStr= "412-555-1212 412-555-1213 412-555-1214"
# regex=re.compile(r"412-(.{8})")
# matches= re.findall(regex, randStr)
# print(len(matches))
# for i in matches:
# 	print(i)
#*******************************
randStr= "My number is 412-555-1212"
regex= re.compile(r"412-(.*)-(.*)")
matches= re.findall(regex, randStr)
print(len(matches))
print(matches[0][0])
print(matches[0][1])