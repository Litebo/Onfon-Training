import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = './fifa21.csv'
df = pd.read_csv(file_path)


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

df['Value'] = df['Value'].apply(convert_monetary_value)
df['Wage'] = df['Wage'].apply(convert_monetary_value)


plt.figure(figsize=(10, 6))
plt.scatter(df['Wage'], df['Value'], alpha=0.5)
plt.title('Scatter Plot between Wage and Value')
plt.xlabel('Wage (in Euros)')
plt.ylabel('Value (in Euros)')
plt.grid(True)
plt.show()


underpaid_players = df[(df['Value'] > df['Value'].mean()) & (df['Wage'] < df['Wage'].mean())]
print(underpaid_players[['Name', 'Club', 'Value', 'Wage']])
