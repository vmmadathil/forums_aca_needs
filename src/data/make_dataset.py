import pandas as pd
import re



def cleancsv(input_filepath, output_filepath):
    df = pd.read_csv(input_filepath)

    #filtering out entries that have no text
    df = df[df['selftext'].notnull()]

    #converting to time stamp and dropping unnecessary columns
    df['time_created'] = pd.to_datetime(df['created_utc'], unit='s')
    df = df.drop(columns = ['url', 'created_utc', 'created'])

    #processing text
    #removing strings that have urls
    df['processed_text'] = df['selftext'].map(lambda x: re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',"",x,flags=re.MULTILINE))
    #df['processed_text'] = df['selftext'].map(lambda x: re.sub(r'^www\/\/.*[\r\n]*','', x, flags=re.MULTILINE))


    #removing puncutation
    df['processed_text'] = df['processed_text'].map(lambda x: re.sub('[,\.!?]', '', x))

    #lowercasing all the words
    df['processed_text'] = df['processed_text'].map(lambda x: x.lower())

    #printing out the first 5 rows
    print(df.head())

    #printing to csv
    df.to_csv(output_filepath, index=False)


""" 
Runs data processing scripts to turn raw data from (../raw) into
cleaned data ready to be analyzed (saved in ../processed).
"""
def main(input_filepath, output_filepath):
    
    cleancsv(input_filepath, output_file)

if __name__ == '__main__':
    input_file = '../../data/raw/raw_reddit_scrap.csv'
    output_file = '../../data/processed/cleaned_reddit_data.csv'

    main(input_file, output_file)
