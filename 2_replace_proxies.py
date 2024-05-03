import pandas as pd
import requests

# Read the CSV file into a DataFrame
df = pd.read_excel('test.xlsx')

# Function to get the final redirected URL
def get_redirected_url(row):
    url = row['news_link']
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
        }
        response = requests.get(url, headers=headers, timeout=5)
        return response.url
    except requests.exceptions.RequestException as e:
        print(f"Exception at row {row.name}: {e}")
        return url

# Apply the function to the DataFrame
df['news_link'] = df.apply(get_redirected_url, axis=1)

# Save the DataFrame back to the CSV file
df.to_csv('file_test.csv', index=False)
