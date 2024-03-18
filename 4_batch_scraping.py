import pandas as pd
import Scraping
from urllib.parse import urlparse

# Mapping of website names to their corresponding functions
website_to_function = {
    'nbcnews.com': 'NBC',
    'msnbc.com': 'MSNBC',
    'alternet.org': 'alternet',
    'breitbart.com': 'breitbart',
    'thefederalist.com': 'thefederalist',
    'usatoday.com': 'usatoday',
    'huffpost.com': 'huffpost',
    'foxnews.com': 'foxnews',
    'foxbusiness.com': 'foxbusiness',
    'thedailybeast.com': 'thedailybeast'
}

def process_links(start_index=0):
    # Read the CSV file
    df = pd.read_csv('test.csv')

    # Open the error list file in append mode
    with open('error_list.txt', 'a') as error_file:
        # Iterate over each row in the DataFrame, starting from start_index
        for index, row in df.loc[start_index:].iterrows():
            # Get the news link
            news_link = row['news_link']
            
            # Parse the URL and extract the netloc
            netloc = urlparse(news_link).netloc
            
            # Extract the second-level and top-level domain
            domain = '.'.join(netloc.split('.')[-2:])
            
            # Check if the domain is in the list of known websites
            if domain in website_to_function:
                # Call the appropriate function and save the output
                getattr(Scraping, website_to_function[domain])(news_link, f'{index}.txt')
            else:
                # Write an error message to the error list file
                error_file.write(f'Row {index}: Unknown website "{domain}"\n')

# Call the function with the desired start index
process_links(start_index=1120)
