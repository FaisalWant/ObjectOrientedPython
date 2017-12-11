# functions defining the services
import MySQLdb
def getCarats(myvar):
   mydb = MySQLdb.connect(host='localhost',user='root',passwd='faisal123',db='blog_data')
   cursor = mydb.cursor()
   myList=list()
   cursor.execute('SELECT' +' '+ myvar+ ' '+'from testcsv')
   for i  in cursor.fetchall():
      myList.append(i)
   #newList=[str(var).strip('(,)') for var in myList]
   #print(newList)
   return (str(myList[0]).strip('(,)'))
print(getCarats('carat'))