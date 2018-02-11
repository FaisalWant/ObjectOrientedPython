# # 
# create a file name mydata2.txt
# open a file without without
# catch file not FoundError
# In else print contents
# in finally 
# open non existant file my data3.txt

try:
  f= open("newFile.txt", encoding="utf-8")
  
except FileNotFoundError as ex:
    print("Sorry pal that file doesn't exist")
    print(ex.args)

finally:
	print("Hey pall file is open")
  

