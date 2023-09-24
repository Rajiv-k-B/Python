

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file='data_file.xlsx'

xl = pd.ExcelFile(file) #Read from Excel
dfs = xl.parse(xl.sheet_names[0])# Parsing the Excel sheet to data frame

dfs = list(dfs['Timeline'])# Timeline is the column name, and these line of code will remove the blace lines

print(dfs)

sid = SentimentIntensityAnalyzer()

str1="UTC+05:30"

for data in dfs:
    a=data.find(str1)
    if(a==-1):
         ss=sid.polarity_scores(data)
         print(data)
         for k in ss:
             print(k,ss[k])