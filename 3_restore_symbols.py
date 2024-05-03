import pandas as pd

# Load the dataframes
old_df = pd.read_excel('final_labels_SG1.xlsx')
new_df = pd.read_excel('file_test.xlsx')

# Function to keep only basic English alphabets
def only_english_alphabets(s):
    return ''.join(c for c in s if c.isalpha() and ord(c) < 128)

# Create a dictionary to store the basic English alphabetic form of each text in the old file
old_dict = {only_english_alphabets(text): text for text in old_df['text']}

for i in range(len(new_df)):
    new_text = new_df.loc[i, 'text']
    new_text_alpha = only_english_alphabets(new_text)
    
    # If the basic English alphabetic form of the new text is in the dictionary, replace it
    if new_text_alpha in old_dict:
        new_df.loc[i, 'text'] = old_dict[new_text_alpha]
        
new_df.to_csv('test.csv', index=False)
