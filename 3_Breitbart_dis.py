import pandas as pd


# Load your dataset
df = pd.read_csv('test.csv')

# Discard all rows that contain 'feedproxy.google.com'
df = df[~df['news_link'].str.contains('feedproxy.google.com')]





# Save the updated dataset
df.to_csv('file.csv', index=False)
