#matchEmailAddr.py
# 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# An @ symbol
# 2 to 20 lowercase and uppercase letters, numbers, plus.-
# A period
# 2-3 lowercase and uppercase letters
import re
emailList="@gmail.com"
if re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}",emailList):
   print("match")