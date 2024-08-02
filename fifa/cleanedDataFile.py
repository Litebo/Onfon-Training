import pandas as pd

# Load the CSV file
file_path = './fifa21.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand the structure
print(df.head())

# Remove newline characters from all columns
df = df.applymap(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)

# Function to convert height in the format '5'7"' to inches
def convert_height(height):
    try:
        feet, inches = height.split("'")
        return int(feet) * 12 + int(inches.replace('"', ''))
    except:
        return None

# Function to convert weight in the format '165lbs' to integer
def convert_weight(weight):
    try:
        return int(weight.replace('lbs', ''))
    except:
        return None

# Apply the conversion functions to the relevant columns
df['Height'] = df['Height'].apply(convert_height)
df['Weight'] = df['Weight'].apply(convert_weight)

# Display the first few rows of the dataframe to verify the changes
print(df.head())

# Optionally, save the cleaned dataframe to a new CSV file
df.to_csv('./fifa21_cleaned_data.csv', index=False)
