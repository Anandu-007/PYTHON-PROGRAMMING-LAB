import json
import pandas as pd

data = '''
{
    "cities": [
        {"location": "Thrissur", "temperature": 30, "humidity": 70},
        {"location": "Kochi", "temperature": 32, "humidity": 75},
        {"location": "Kozhikode", "temperature": 29, "humidity": 80}
    ]
}
'''

# Parse JSON data
weather = json.loads(data)

# Convert JSON into a table
df = pd.DataFrame(weather["cities"])

print("Weather Report:")
print(df)

# Generate summary
print("Average Temperature:", df["temperature"].mean())
print("Average Humidity:", df["humidity"].mean())