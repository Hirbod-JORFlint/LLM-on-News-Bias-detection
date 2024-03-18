import pandas as pd
import re

# This script extract train dataset from the big dataset.
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text

# Step 1: Read CSV files into pandas DataFrames with specified encoding
#annotations_df = pd.read_excel('labeled_dataset.xlsx')
annotations_df = pd.read_csv('labeled_dataset_annotation.csv')
train_df = pd.read_csv('test.csv', encoding='utf-8')

# Step 2: Identify dropped rows and create a DataFrame with all fields
dropped_rows = []
dropped_rows_all_fields = []
for index, row in annotations_df.iterrows():
    if clean_text(row['sentence']) in train_df['text'].apply(clean_text).values:
        dropped_rows_all_fields.append(row)
    else:
        dropped_rows.append(row)

# Step 3: Save modified DataFrame (without dropped rows) as new CSV file in original format
annotations_without_dropped_df = pd.DataFrame(dropped_rows)
annotations_without_dropped_df.to_csv('new_file.csv', index=False, encoding='utf-8')

# Step 4: Save dropped rows (all fields) into a new CSV file with original format
dropped_rows_df = pd.DataFrame(dropped_rows_all_fields)
dropped_rows_df.to_csv('dropped_rows.csv', index=False, encoding='utf-8')
