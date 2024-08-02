import pandas as pd
from datetime import datetime

# Load the CSV file
file_path = '/fifa21.csv'
df = pd.read_csv(file_path)

# Remove newline characters from all columns
df = df.applymap(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)

# Function to convert height in the format '5\'7"' to inches
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

# Function to convert monetary values to numerical values
def convert_monetary_value(value):
    try:
        if 'M' in value:
            return float(value.replace('M', '').replace('€', '')) * 1_000_000
        elif 'K' in value:
            return float(value.replace('K', '').replace('€', '')) * 1_000
        else:
            return float(value.replace('€', ''))
    except:
        return None

# Function to remove star characters and convert to numerical values
def convert_star_values(value):
    try:
        return int(value.replace('★', '').strip())
    except:
        return None

# Apply the conversion functions to the relevant columns
df['Height'] = df['Height'].apply(convert_height)
df['Weight'] = df['Weight'].apply(convert_weight)
df['Value'] = df['Value'].apply(convert_monetary_value)
df['Wage'] = df['Wage'].apply(convert_monetary_value)
df['Release Clause'] = df['Release Clause'].apply(convert_monetary_value)

# Assuming the columns with star characters are named 'Skill Moves' and 'Weak Foot'
df['Skill Moves'] = df['Skill Moves'].apply(convert_star_values)
df['Weak Foot'] = df['Weak Foot'].apply(convert_star_values)

# Parse the 'Joined' column to extract the year
df['Joined'] = pd.to_datetime(df['Joined'], errors='coerce')

# Calculate the number of years each player has been at their club
current_year = datetime.now().year
df['Years at Club'] = current_year - df['Joined'].dt.year

# Identify players who have been at their club for more than 10 years
long_term_players = df[df['Years at Club'] > 10]

# Display the relevant information for these players
print(long_term_players[['Name', 'Club', 'Joined', 'Years at Club', 'Value', 'Wage', 'Release Clause', 'Skill Moves', 'Weak Foot']])

# Optionally, save the cleaned dataframe to a new CSV file
df.to_csv('/mnt/data/fifa21_cleaned_data.csv', index=False)

# Optionally, save the filtered data to a new CSV file
long_term_players.to_csv('/stars_to_numerical_values.csv', index=False)
