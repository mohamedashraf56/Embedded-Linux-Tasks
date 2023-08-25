#!/usr/bin/python3

import requests

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data

# Get your public IP address
ip = requests.get('https://api.ipify.org').text

# Get location information based on IP address
location_data = get_location(ip)

# Extract relevant information
city = location_data['city']
region = location_data['region']
country = location_data['country_name']

# Print location information
print("Your location:")
print("City:", city)
print("Region:", region)
print("Country:", country)
