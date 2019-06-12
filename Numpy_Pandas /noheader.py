# noheader.py
import pandas as pd

# skipping first  four rows as they are not needed

movies_skip_rows=pd.read_excel("movies-no-header.xls", header=None, skiprows=4)
movies_skip_rows.head(5)


# Assinging  a column header to the different columns

movies_skip_rows.columns=['Title', 'Year','Genre', 'Language', 'Country', 'Content Rating',
                           'Duration', 'Aspect Ratio', 'Budget', 'Gross Earnings', 'Director', 
                           'Actor 1','Actor 2','Actor 3', 'Facebook likes - Director', 
                            'Facebook Likes -Actor 1', 'Facebook Likes -Actor 2', 'Facebook Likes -Actor 3', 
                            'Facebook Likes - Cast Total', 'Facebook Likes- Movie', 'Facenumber in posters', 'User Votes',
                            'Reviews by Users', 'Reviews by Critics', 'IMDB Scores' ]

movies_skip_rows.head()                            