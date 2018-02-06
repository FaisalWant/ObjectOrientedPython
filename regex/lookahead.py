#lookahead.py
import re
#(?=expression)
# randStr= "One two three four"
# regex= re.compile(r"\w+(?=\b)")
# matches= re.findall(regex, randStr)
# for i in matches:
# 	print(i)

# lookbehind.

# randStr= "1. Bread 2. Apples 3. lettuce"

# regex= re.compile(r"(?<=\d.\s)\w+")
# matches= re.findall(regex, randStr)
# for i in matches:
# 	print(i)


# lookahead and lookbehind
randStr= "<h1> i'm important</h1> <h1> So am I</h1>"
regex= re.compile(r"(?<=<h1>).+?(?=</h1>)")
matches= re.findall(regex, randStr)
for i in matches:
	print(i)