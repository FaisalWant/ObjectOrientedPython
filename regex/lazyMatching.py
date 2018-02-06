import re
randStr= "<name> Life of Mars</name><name>Freaks and Greeks</name>"
regex= re.compile("<name>.*?</name>")
matches= re.findall(regex,randStr)
for i in matches:
   print(i)