import requests

API_KEY = "470ebec4c2dfaaaa45363e8b5c90ba07"
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather_data(location):
    try:
        url = f"{BASE_URL}?q={location}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        response.raise_for_status() 
        
        weather_data = response.json()
        
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        
        return {
            'temperature': temp,
            'humidity': humidity,
            'description': description
        }
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    
    return None

def validate_input(user_input):
    return user_input.strip() != ''

def main():
    print("Welcome to the Weather Program!")
    
    while True:
        user_input = input("Enter a city name or ZIP code (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if validate_input(user_input):
            weather = get_weather_data(user_input)
            if weather:
                print(f"Current weather in {user_input.capitalize()}:")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Description: {weather['description'].capitalize()}")
            else:
                print("Could not retrieve weather data. Please try again.")
        else:
            print("Invalid input. Please enter a valid city name or ZIP code.")

if __name__ == "__main__":
    main()



