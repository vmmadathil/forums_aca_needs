'''
This script will scrape the health insurance subreddit for posts relating to the ACA
'''
from psaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()

#calling the function to fetch all the posts
gen = api.search_submissions(subreddit= 'HealthInsurance',
                             after= 1356998400,
                             filter = ['url', 'title', 'selftext', 'created_utc'])


#converting to dataframe and appending to the list
df  = pd.DataFrame([thing.d_ for thing in gen])

print(df.info())

print('finished scraping, saving to csv')

#print to a csv
df.to_csv('../data/raw/raw_reddit_scrap.csv')

print('saved to csv')