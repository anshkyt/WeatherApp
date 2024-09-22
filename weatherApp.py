import requests
def get_weather(api_key, location):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric")  # Construct the URL for the API request with the given location and API key
   
    if response.status_code == 200:  # Check if the response status code is 200 (OK)
        data = response.json() # Parse the JSON response content
        weather = { # Extract relevant weather information from the parsed JSON
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        return None

api_key = 'b47213758248260beb15e16890fe2a7e'
location = input("Type a location you want the weather of: ")
weather_info = get_weather(api_key, location) # Call the get_weather function with the API key and location
if weather_info:
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Description: {weather_info['description']}")
else:
    print("Failed to get weather data")
