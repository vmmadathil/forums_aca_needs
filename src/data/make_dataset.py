import pandas as pd
import re
from nltk.corpus import stopwords
import redditcleaner


def cleancsv(input_filepath, output_filepath):
    df = pd.read_csv(input_filepath, encoding='utf-8')

    #filtering out entries that have no text
    df = df[df['selftext'].notnull()]

    #filtering out entries that have no title
    df = df[df['title'].notnull()]

    #converting to time stamp and dropping unnecessary columns
    df['time_created'] = pd.to_datetime(df['created_utc'], unit='s')
    df = df.drop(columns = ['url', 'created_utc', 'created'])

    #removing rows that are deleted, removed, and blank comments
    df = df.loc[df['selftext'] != '[deleted]']
    df = df.loc[df['selftext'] != '[removed]']
    df = df.loc[df['selftext'] != '']

    #removing rows that are deleted, removed, and blank titles
    df = df.loc[df['title'] != '[deleted]']
    df = df.loc[df['title'] != '[removed]']
    df = df.loc[df['title'] != '']

    #processing text
    df['processed_text'] = df['selftext'].map(redditcleaner.clean)

    #removing blank comments
    df = df.loc[df['processed_text'] != '']

    #removing puncutation
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub('[,;\!?]', '', x))

    #removing any missed urls
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',"",x,flags=re.MULTILINE))
   
    #removing puncutation
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub('[,;\.!?]', '', x))

    #removing parentheses
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub('[()]' ,'', x))

    #fixing apostrophes
    #df['processed_text'] = df['processed_text'].replace({"â€™" : "'"}, regex=True)

    #lowercasing all the words
    df['processed_text'] = df['processed_text'].map(lambda x: x.lower())

    #removing stopwords
    stop = stopwords.words('english')
    df['processed_text'] = df['processed_text'].apply(lambda x: ' '.join([item for item in str.split(x) if item not in stop]))

    #removing abbreviations
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub('y/o' ,'year old', x))

    #removing posts that have any NAs or blank commends
    df = df.loc[df['processed_text'] != '']
    df = df.dropna()

    #---------------------------------------------------
    #---------------------------------------------------
    #now doing the same process for titles 

    #processing text
    df['processed_title'] = df['title'].map(redditcleaner.clean)

    #removing blank comments
    df = df.loc[df['processed_title'] != '']

    #removing puncutation
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub('[,;\!?]', '', x))

    #removing any missed urls
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',"",x,flags=re.MULTILINE))
   
    #removing puncutation
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub('[,;\.!?]', '', x))

    #lowercasing all the words
    df['processed_title'] = df['processed_title'].map(lambda x: x.lower())

    #removing parentheses and brackets
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub('[()]' ,'', x))
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub('[\[\]]' ,'', x))

    #removing abbreviations
    df['processed_title'] = df['processed_title'].map(lambda x: re.sub('y/o' ,'year old', x))

    #removing posts that have any NAs or blank commends
    df = df.loc[df['processed_title'] != '']
    df = df.dropna()

    #removing stopwords
    stop = stopwords.words('english')
    df['processed_title_no_stop'] = df['processed_title'].apply(lambda x: ' '.join([item for item in str.split(x) if item not in stop]))

    #printing out the first 5 rows 
    print(df.head())

    #printing to csv
    df.to_csv(output_filepath, index=False, encoding='utf-8-sig')


""" 
Runs data processing scripts to turn raw data from (../raw) into
cleaned data ready to be analyzed (saved in ../processed).
"""
def main(input_filepath, output_filepath):
    
    cleancsv(input_filepath, output_file)

if __name__ == '__main__':
    input_file = '../../data/raw/raw_reddit_scrape_3.csv'
    output_file = '../../data/processed/cleaned_reddit_data_3.csv'

    main(input_file, output_file)
