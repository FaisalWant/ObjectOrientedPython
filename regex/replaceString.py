#replaceString.py
import re
owlFood= "rat cat mat pat"
regex=re.compile("[cr]at")
owlFood= regex.sub("owl",owlFood)
print(owlFood)