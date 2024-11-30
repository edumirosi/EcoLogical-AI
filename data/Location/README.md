This includes the data for Location.

This will take the data from EnergyMap and update the .csv file.

1) Step 1: Get all the locations available:
    a) we use get_locations.py to get a zones_data.json file. This .json file includes all the countries used.

2) Step 2: Get the carbon intensity for all the locations:
    b) get all the CO2 comsuptions for the locations, using create_table.py and putting them into .csv file