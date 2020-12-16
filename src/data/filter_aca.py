import pandas as pd

#reading in dataset 
posts = pd.read_csv('../data/processed/cleaned_reddit_data.csv')

#filtering out post titles that don't contain anything about the ACA
posts_aca = posts[posts['processed_title'].str.contains('obamacare|obama care|aca|affordable care act|individual mandate|healthcare.gov|1095-a|1095a|1095|open enrollment|marketplace|aptc|advance premium tax credit|special enrollment|gold|silver|bronze|health insurance exchange|exchange|pre existing|preexisting|pre-existing')]

#printing to file
posts_aca.to_csv('../data/processed/aca_posts.csv')