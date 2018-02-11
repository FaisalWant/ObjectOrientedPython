#negativeLookahead.py
import re
# (?!expression): Negative look behind
randStr= "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex= re.compile(r"(?<!\$)\d+")
matches= re.findall(regex, randStr)
print(len(matches))
matches=[int(i) for i in matches]
from functools import reduce

print("Total items {}". format(reduce((lambda x,y:x+y),matches)))