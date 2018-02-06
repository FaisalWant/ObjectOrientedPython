#backslashes.py
import re
randStr= "Here is \\stuff"
print("find\\stuff:", re.search(r"\\stuff",randStr))