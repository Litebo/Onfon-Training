import pandas as pd
from datetime import datetime

# Load the CSV file
file_path = './fifa21.csv'
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

# Apply the conversion functions to the relevant columns
df['Height'] = df['Height'].apply(convert_height)
df['Weight'] = df['Weight'].apply(convert_weight)

# Parse the 'Joined' column to extract the year
df['Joined'] = pd.to_datetime(df['Joined'], errors='coerce')

# Calculate the number of years each player has been at their club
current_year = datetime.now().year
df['Years at Club'] = current_year - df['Joined'].dt.year

# Identify players who have been at their club for more than 10 years
long_term_players = df[df['Years at Club'] > 10]

# Display the relevant information for these players
print(long_term_players[['Name', 'Club', 'Joined', 'Years at Club']])

# Optionally, save the filtered data to a new CSV file
long_term_players.to_csv('./fifa21_10yearsPlayers.csv', index=False)
