import pandas as pd
import re

#reading in dataset 
posts = pd.read_csv('../../data/processed/cleaned_reddit_data_3.csv')
print('filtering....')

#filtering out post titles that don't contain anything about the ACA
posts_aca = posts[posts['processed_title'].str.contains('obamacare|obama care|aca|affordable care act|individual mandate|healthcare.gov|1095-a|1095a|1095|open enrollment|marketplace|aptc|advance premium tax credit|special enrollment|gold|silver|bronze|health insurance exchange|exchange|pre existing|preexisting|pre-existing|tax credit')]

#ensuring that preexisting is uniform 
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'pre-existing': 'preexisting'}, regex = True) 
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'pre existing': 'preexisting'}, regex = True)

#ensuring ACA references are uniform 
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'affordable care act': 'aca'}, regex = True)
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'obamacare': 'aca'}, regex = True)
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'obama care': 'aca'}, regex = True)

#some other abbreviations
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'health savings account': 'hsa'}, regex = True)
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'health care': 'healthcare'}, regex = True)

# removing unnecessary instances of the word "health" 
posts_aca['processed_title'] = posts_aca['processed_title'].replace({'health insurance': 'insurance'}, regex = True)

### No stop column
#ensuring that preexisting is uniform 
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'pre-existing': 'preexisting'}, regex = True) 
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'pre existing': 'preexisting'}, regex = True)

#ensuring ACA references are uniform 
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'affordable care act': 'aca'}, regex = True)
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'obamacare': 'aca'}, regex = True)
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'obama care': 'aca'}, regex = True)

#some other abbreviations
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'health savings account': 'hsa'}, regex = True)
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'health care': 'healthcare'}, regex = True)

# removing unnecessary instances of the word "health" 
posts_aca['processed_title_no_stop'] = posts_aca['processed_title_no_stop'].replace({'health insurance': 'insurance'}, regex = True)

#printing to file
posts_aca.to_csv('../../data/processed/aca_posts_3.csv', index=False)

print("complete!")