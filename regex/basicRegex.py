#basicRegex.py
import re
# if re.search("ape","The ape was at the apex"):
#    print("There is an ape")

# allApes= re.findall("ape.","the ape was at the apex")
# for i in allApes:
#     print(i
#******************
# theStr= "The ape was at the apex"
# for i in re.finditer("ape.",theStr):
# 	locTuple =i.span()  #span returns a tuple
# 	print(locTuple)
# 	print(theStr[locTuple[0]:locTuple[1]])
#**************************
# animalStr= "Cat rat mat pat"
# allAnimals= re.findall("[crmfp]at",animalStr)
# for i in allAnimals:
# 	print(i)
#**************************


# animalStr= "Cat rat mat pat"
# someAnimals= re.findall("[c-mC-M]at",animalStr)
# for i in someAnimals:
# 	print(i)

animalStr= "Cat rat mat pat"
someAnimals= re.findall("[^Cr]at",animalStr)
for i in someAnimals:
 	print(i)