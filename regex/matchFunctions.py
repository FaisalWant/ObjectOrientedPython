#matchFunctions.py

import re

# match= re.search(r"\d{2}", "The chicked weighted 13 lbs")
# print("match",match.group())
# print("Span", match.span())
# print("Start", match.start())
# print("End",match.end())

#********************************
#named group examples
# randStr= "December 21 1974"
# regex= r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
# matches= re.search(regex, randStr)
# print("Month:",  matches.group('month'))
# print("Day:", matches.group('day'))
# print("Year",matches.group('year'))


#*************************************
# randStr= "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
# regex=re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# matches=re.findall(regex,randStr)
# for i in matches:
#    print(i)
#**************************************
randStr= "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"


regex= re.compile(r"( (1?)(-| ?)(\()?(\d{3}(\)|-| |\)-|\)?(\d{3})(-|)?(\d{4}|\d{4}) )")
matches= re.findall(regex, randStr)
for i in matches:
	print(i)