# excel_Pandas.py
# reading excel in pandas
import pandas as pd
#import matplotlib.pyplot as plt
excel_file= 'movies.xls'

# reading the first excel sheet
movie= pd.read_excel(excel_file, sheetname=0, index_col=0)
movie2= pd.read_excel(excel_file, sheetname=1, index_col=0)
movie3=pd.read_excel(excel_file, sheet_name=2, index_col=0)
# print ("Printing Head of Excel:", movie.head())
# print("Printing Head of Excel Sheet Second:", movie2.head())
# print("Printing Head of Excel Sheet thrid:", movie3.head())

# concatenating different sheets of excel

movies4= pd.concat([movie, movie2, movie3])
print(movies4.shape)


#################################################
# using the Excel File to read mulitple sheets

xlsx= pd.ExcelFile(excel_file)

movies_sheet=[]
for sheet in xlsx.sheet_names:
	movies_sheet.append(xlsx.parse(sheet))
movies=pd.concat(movies_sheet)

print (movies.shape)


# sort values based on some criteria


# sorted_by_gross= movies.sort_values(['Gross Earnings'], ascending= False)
# sorted_by_gross.head(10).plot(kind="barh")
# plt.show()

# # displaying as histogram

# movies['IMDB score'].plot(kind= "hist")
# plt.show
print(movies.describe())




# Reading a subset of Columns

print("*" *10)
print("Reading a subset of Columns")

movies_subset_columns= pd.read_excel(excel_file, parse_cols=6)
print(movies_subset_columns.head())



# Applying formula's on the individual columns

movies["Net Earnings"]= movies["Gross Earnings"] - movies["Budget"]
sorted_movies= movies[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
sorted_movies.head(10)['Net Earnings'].plot.barh()
plt.show()




# Pivot Table in Python

movies_subset= movie[['Year', 'Gross Earnings']]
movies_subset.head()

earnings_by_year= movies_subset.pivot_table(index=['Year'])
print(earnings_by_year.head())



# Exporting Valus out of pandas into excel

#movies.to_excel('output.xlsx')
# By default, the index is also saved to the output file.
# However, sometimes the index doesn't provide any useful information. 


#----movies.to_excel('output.xlsx',index=False)




# making output file look nice using ExcelWriter class


writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
movies.to_excel(writer, index=False, sheet_name='report')
workbook = writer.book
worksheet = writer.sheets['report']
header_fmt = workbook.add_format({'bold': True})
worksheet.set_row(0, None, header_fmt)
writer.save()



