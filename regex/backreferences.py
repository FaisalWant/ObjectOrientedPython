#backreferences.py
import re
# randStr= "the cat cat fell out the window"
# regex= re.compile(r"(\b\w+)\s+\1")
# matches= re.findall(regex,randStr)
# print("Matches:",len(matches))
# for i in matches:
# 	print(i)

#**********************************************
# randStr= "<a href='#'><b> The Link</b></a>" 
# regex= re.compile(r"<b>(.*?)</b>")
# randStr= re.sub(regex,r"\1",randStr)
# print(randStr)
# matches= re.findall(regex,randStr)
# print("Matches:",len(matches))
# for i in matches:
# 	print(i)	
#**********************************************
randStr="412-555-1212"
regex= re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
randStr= re.sub(regex,r"(\1)\2",randStr)
print(randStr)
