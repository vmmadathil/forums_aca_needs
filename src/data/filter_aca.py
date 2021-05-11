import pandas as pd
import re

#reading in dataset 
posts = pd.read_csv('../../data/processed/cleaned_reddit_data_3.csv')
print('filtering....')

#filtering out post titles that don't contain anything about the ACA
posts_aca = posts[posts['processed_title'].str.contains('obamacare|obama care|aca|affordable care act|individual mandate|healthcare.gov|1095-a|1095a|1095|open enrollment|marketplace|aptc|advance premium tax credit|special enrollment|gold|silver|bronze|health insurance exchange|exchange|pre existing|preexisting|pre-existing|tax credit')]

#ensuring that preexisting is uniform 
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'pre-existing': 'preexisting'}, regex=True)
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'pre existing': 'preexisting'}, regex=True)

#printing to file
posts_aca.to_csv('../../data/processed/aca_posts_3.csv', index=False)

print("complete!")