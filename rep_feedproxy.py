import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def get_original_link(query):
    # DuckDuckGo search URL
    search_engine_url = "https://duckduckgo.com/?q"
    # Add the necessary parameters for DuckDuckGo
    response = requests.get(search_engine_url + query + "&va=c&t=hk&ia=web")
    soup = BeautifulSoup(response.text, 'html.parser')
    # This assumes that the first link in the search results is the original article
    # You may need to adjust this depending on the structure of the search engine's results page
    link = soup.find('a')['href']
    return link

# Load your dataset
df = pd.read_csv('dataset.csv')

# Loop through each row in the dataset
for index, row in df.iterrows():
    if 'feedproxy.google.com' in row['news_link'] and row['outlet'] == 'Breitbart':
        # Use the text of the article as the search query
        # Replace white spaces with '+'
        text_with_plus = row['text'].replace(' ', '+')
        # Remove non-alphanumeric characters (except '+')
        clean_text = re.sub(r'[^A-Za-z0-9+]+', '', text_with_plus)
        query = clean_text + ' site:breitbart.com'
        original_link = get_original_link(query)
        # Replace the old link with the original link
        df.at[index, 'news_link'] = original_link

# Save the updated dataset
df.to_csv('updated_dataset.csv', index=False)
