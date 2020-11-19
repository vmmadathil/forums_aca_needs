'''
This script will scrape the health insurance subreddit for posts relating to the ACA
'''
from psaw import PushshiftAPI
import pandas as pd
import datetime

api = PushshiftAPI()

#starting and ending epoch dates
curr_epoch = 1605772907
end_epoch = 1605757257

print('beginning scraping')

#getting the comments with 1000 post batches
while (curr_epoch >= end_epoch):
    gen = api.search_submissions(subreddit='HealthInsurance',
                                after=curr_epoch,
                                filter = ['url', 'title', 'selftext', 'created_utc'],
                                limit = 1000)
    #converting to dataframe and appending to the list
    df  = pd.DataFrame([thing.d_ for thing in gen])
    li.append(df)

    #setting current date as latest processed date
    curr_epoch = df['created_utc'].tail(1) 
    
    #printing progress message
    curr_time = datetime.datetime.fromtimestamp(curr_time)
    print("Currently scraped until {}").format(curr_time)

    filename = ('raw_scrape_{}.csv').format(curr_time)

    #saving to csv
    df.to_csv(filename)

print('finished scraping')
