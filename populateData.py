import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',user='root',passwd='faisal123',db='blog_data')
cursor = mydb.cursor()
cursor.execute("create table IF NOT EXISTS testcsv(carat float, cut varchar(20), color varchar(20),clarity varchar(20) ,depth float, dtable float, price float , x float, y  float , z float )" )


with open("diamonds.csv",'r') as f:
  with open("refined.csv","w") as result:
    read = csv.reader(f)
    next(read)    # Skip the first 'title' row.
    wtr= csv.writer( result )
    for r in read :
       wtr.writerow((r[1], r[2],r[3], r[4] ,r[5],r[6],r[7],r[8],r[9],r[10]))

with open ('refined.csv') as z:
   csv_data=csv.reader(z)
   for row in csv_data:
   	   #print(float(row[0]),row[1],row[2],row[3],float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]))
# #close the connection to the database.
       cursor.execute('INSERT INTO testcsv(carat, cut, color,clarity,depth,dtable,price,x, y, z ) VALUES("%f", "%s", "%s","%s","%f","%f","%f","%f","%f","%f")' %(float(row[0]),row[1],row[2],row[3],float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9])))
# #close the connection to the database.

mydb.commit()
cursor.close()



