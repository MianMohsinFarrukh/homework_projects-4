import requests

def get_weather(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        # Extract weather details
        weather = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

def main():
    print("Welcome to the Weather Program!")
    location = input("Enter the city name: ")
    api_key = ""  # Replace with your actual API key
    
    weather_details = get_weather(location, api_key)
    if isinstance(weather_details, dict):
        print("\nWeather Details:")
        print(f"Location: {weather_details['location']}")
        print(f"Temperature: {weather_details['temperature']}°C")
        print(f"Description: {weather_details['description']}")
        print(f"Humidity: {weather_details['humidity']}%")
        print(f"Wind Speed: {weather_details['wind_speed']} m/s")
    else:
        print(weather_details)

if __name__ == "__main__":
    main()
