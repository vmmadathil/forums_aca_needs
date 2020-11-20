import pandas as pd
from datetime import datetime



def cleancsv(input_filepath):
    df = pd.read_csv(input_filepath)

    

    #df['time_created'] = datetime.fromtimestamp(df['created_utc'].astype(float))
    df = df.drop(columns = ['url'])

    print(df.head())





""" 
Runs data processing scripts to turn raw data from (../raw) into
cleaned data ready to be analyzed (saved in ../processed).
"""
def main(input_filepath, output_filepath):
    
    cleancsv(input_filepath)

if __name__ == '__main__':
    input_file = '../../data/raw/raw_reddit_scrap.csv'
    output_file = '../../data/process/cleaned_reddit_data.csv'

    main(input_file, output_file)
