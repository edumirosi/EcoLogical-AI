import requests
import json
import pandas as pd
import time

# Your API Token
api_token = 'eMxTt4QXvbg00'

# Base URL with fallback disabled
base_url = 'https://api.electricitymap.org/v3/carbon-intensity/latest'

# Headers for the API request
headers = {'auth-token': api_token}

# Step 1: Read zones_data.json to get country siglas and names
with open('zones_data.json', 'r') as file:
    zones_data = json.load(file)

# Prepare list of countries
countries = [{"sigla": code, "name": details["zoneName"]} for code, details in zones_data.items()]

# Initialize a list to hold the final table data
table_data = []

# Step 2: Fetch Carbon Intensity for each country
for country in countries:
    sigla = country["sigla"]
    name = country["name"]
    
    # Construct the URL with the fallback disabled
    request_url = f"{base_url}?zone={sigla}&shouldUseFallbackCallerLookup=false"
    
    try:
        # Record start time
        start_time = time.time()
        
        # Make API request
        response = requests.get(request_url, headers=headers)
        
        # Record end time
        end_time = time.time()
        
        # Calculate duration
        request_duration = end_time - start_time
        
        # Log the time taken for the request
        print(f"Request for {name} ({sigla}) took {request_duration:.2f} seconds.")
        
        if response.status_code == 200:
            data = response.json()
            carbon_intensity = data.get("carbonIntensity", "N/A")
        else:
            carbon_intensity = "N/A"  # If API fails, mark it as unavailable
    except Exception as e:
        carbon_intensity = "N/A"
        print(f"Error fetching data for {sigla}: {e}")
    
    # Append data to the table list
    table_data.append({
        "Country Sigla": sigla,
        "Country Name": name,
        "Carbon Intensity": carbon_intensity
    })

    # Rate limiting to avoid overloading the API
    time.sleep(0.01)  # Adjust based on the API rate limits

# Step 3: Create DataFrame and Save the Table
df = pd.DataFrame(table_data)
df.to_csv('carbon_intensity_with_times.csv', index=False)
print("Table saved as carbon_intensity_table.csv")

# Optional: Display the table
print(df)
