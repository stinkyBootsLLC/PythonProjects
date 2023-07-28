# docs => https://pandas.pydata.org/
import pandas as pd

# get the csv file as a data frame (df)
df = pd.read_csv('data/survey_results_public.csv')

# shape returns a tuple representing the dimensionality of the DataFrame (rows and columns).
# print(f'This data frame contains {df.shape[0]} rows X {df.shape[1]} columns')
# print()

# get the column names and data types. note: here, object are usually strings 
# print(df.info(verbose=True))
# Prints a summary of columns count and its dtypes but not per column information
# print(df.info(verbose=False)) 

# this file contains the questions that corespond to the anwsers in survey_results_public.csv file
# for example the column Hobbyist	means -> Do you code as a hobby?
schema_df = pd.read_csv('data/survey_results_schema.csv')

# print(f'This survey contains {df.shape[0]} responses from {df.shape[1]} questions')
# print(f'{df.shape[0]} people took this survey')
# print()

# what if i just want to see the first 5 rows of this data?
# print(df.head)
# print()

# how about just the first 2?
# print(df.head(2))
# print()

# you can also get the last rows
# print(df.tail(10))
# print()

# accessing column values is very similar to the way its done with dictionaries (key and value)
# first I will need the column names
# print(df.columns)
# print(schema_df['question'])  
# print()
# print(df['EdLevel'])  'Bachelor’s degree (B.A., B.S., B.Eng., etc.)'
# or 
# educ_vals = list(df.EdLevel)
# print(type(educ_vals))
print(len(df[df['EdLevel']=='Bachelor’s degree (B.A., B.S., B.Eng., etc.)']))
print(f'This data frame contains {df.shape[0]} rows X {df.shape[1]} columns')