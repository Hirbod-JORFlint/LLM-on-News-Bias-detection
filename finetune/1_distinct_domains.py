import pandas as pd
from urllib.parse import urlparse

def extract_domain(url):
    if isinstance(url, str):  # Check if the url is a string
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        return domain
    else:
        return None

# Read the CSV file into a DataFrame
df = pd.read_csv('test.csv')

# Extract the domains
df['news_link'] = df['news_link'].astype(str)
df['domain'] = df['news_link'].apply(extract_domain)

# Get distinct domains
distinct_domains = df['domain'].unique()

# Print them
for domain in distinct_domains:
    print(domain)
