import re 
randStr= """ Just some words
            and some more \r and more
            """

regex=re.compile("[\w\s]+[\r]?\n")
matches= re.findall(regex,randStr)
for i in matches:
   print(i)            