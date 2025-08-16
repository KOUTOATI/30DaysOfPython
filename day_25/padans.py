import pandas as pd
import numpy as np
df = pd.read_csv('day_25\hacker_news.csv')
# first five rows 
print(df.head(5))
# last five rows
print(df.tail(5))
# the title column as pandas Series
print(df['title'])
# counting the number of rows and columns
print(df.shape)
#filter the titles which contain the word 'python'
python_titles = df[df['title'].str.contains('python', case=False)]
print(python_titles)
#filter the titles which contain the word 'JavaScript'
python_title = df[df['title'].str.contains('JavaScript', case=False)]
print(python_title)
#explore the data 
print(df.describe())