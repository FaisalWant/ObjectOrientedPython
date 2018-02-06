#modifyingUrlList.py
import re
#<a href='https://www.youtube.com'>www.youtube.com</a>
#<a href='https://www.google.com'>www.google.com</a>

randStr= "https://www.youtube.come http://www.google.com"
regex=re.compile(r"(https?://([\w.]+)) ")
randStr= re.sub(regex,r"<a href='\1'>\2</a>\n",randStr)
print(randStr)