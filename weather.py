import requests

# WeatherAPI key
WEATHER_API_KEY = '43f4140f9de4697e6d01683275f8fa56'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}")
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        resp = response.json()
        # print(resp)
        # - Current temperature in Fahrenheit
        current_temp = resp['main']['temp']
        # - The "feels like" temperature
        feels_like = resp['main']['feels_like']
        # - Weather condition (e.g., sunny, cloudy, rainy)
        weather = resp['weather'][0]['main']
        # - Humidity percentage
        humidity = resp['main']['humidity']
        # - Wind speed and direction
        wind_speed = resp['wind']['speed']
        # - Atmospheric pressure in mb
        pressure = resp['main']['pressure']
        # - UV Index value
        # uv_index = resp['main']['uvi']
        # - Cloud cover percentage
        cloud_cover = resp['clouds']['all']
        # - Visibility in miles
        visibility = resp['visibility']

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"Current temperature: {current_temp}°F")
        print(f"Feels like: {feels_like}°F")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Pressure: {pressure} hPa")
        # print(f"UV Index: {uv_index}")
        print(f"Cloud cover: {cloud_cover}%")
        print(f"Visibility: {visibility} meters")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")


if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter the city name: ")
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
    pass
