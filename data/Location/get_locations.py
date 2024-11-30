import requests
import json

# URL of the API
url = 'https://api.electricitymap.org/v3/zones'

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Save the JSON data to a file
    with open('zones_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Data has been saved to zones_data.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)
