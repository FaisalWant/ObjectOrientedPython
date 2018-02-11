# matchingNumber.py
# \d:[0-9]
# \D:[^0-9]
# \w:[a-zA-Z0-9]
#\W:[^a-zA-Z0-9]
#\s:[\f\n\r\t\v]
import re
#*************
# randStr="12345"
# print("Matches:",len(re.findall("\d{5}",randStr)))
#*****************
# numStr= "123 12345 123456 1234567"
# print("Matches:", len(re.findall("\d{5,7}",numStr)))
#**********************

# phNum="412-555-1212"
# if re.search("\w{3}-\w{3}-\w{4}",phNum):
#     print("it is a phone Number")
#****************************
# if re.search("\w{2,20}","ultra"):
# 	print( "it is true")
#****************************
# if re.search("\w{2,20}\s\w{2,20}","FaisalAFzal"):
# 	print( "it is valid")
#*******************************
#print("Matches:",len(re.findall("a+", "a as ape bug")))
