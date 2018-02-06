
import re
bd= input("Enter your birthday(m-d-y):")
bdRegex= re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})",bd)
print ("You were born on", bdRegex.group())
print("Birth Month",bdRegex.group(1))
print("Birth Day",bdRegex.group(2))
print("Birth year",bdRegex.group(3))