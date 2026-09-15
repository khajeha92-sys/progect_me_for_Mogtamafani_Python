import urllib.request
import urllib.parse
import json
import requests

class WeatherClient:
    def init(self, latitude=38.08, longitude=46.29):
        self.latitude = latitude
        self.longitude = longitude
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    def _weather_params(self):
        return {
        "latitude": self.latitude,
        "longitude": self.longitude,
        "current_weather": "true"
        }

    def get_weather_urllib(self):
        query_string = urllib.parse.urlencode(self._weather_params())
        full_url = f"{self.weather_url}?{query_string}"

        try:
            with urllib.request.urlopen(full_url, timeout=10) as response:
                raw_data = response.read().decode("utf-8")
                return json.loads(raw_data)
        except Exception as e:
            print(f"❌ urllib error: {e}")
            return None

    def get_weather_requests(self):
        try:
            response = requests.get(
            self.weather_url,
            params=self._weather_params(),
            timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ requests error: {e}")
            return None

    def compare_urllib_and_requests(self):
        print("Using urllib:")
        data_urllib = self.get_weather_urllib()
        print(data_urllib)

        print("\nUsing requests:")
        data_requests = self.get_weather_requests()
        print(data_requests)

class SafeAPIClient:
    def init(self, timeout=10):
        self.timeout = timeout

    def safe_api_call(self, url, params=None):
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print("⏰ Timeout! The server took too long.")
        except requests.exceptions.ConnectionError:
            print("🌐 Connection error! Please check your internet.")
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            if status_code == 404:
                print("🔍 Not found! (404)")
            elif status_code == 429:
                print("🚦 Too many requests! (429)")
            elif status_code >= 500:
                print("🔧 Server error! Please try again later.")
            else:
                print(f"⚠️ HTTP error {status_code}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

            return None

class CityWeatherApp:
    def init(self):
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.api_client = SafeAPIClient()

    def get_coordinates(self, city_name):
        params = {"name": city_name}
        data = self.api_client.safe_api_call(self.geocoding_url, params=params)

        if not data:
            return None, None, None, None

        results = data.get("results", [])
        if not results:
            print(f"❌ No results found for '{city_name}'")
            return None, None, None, None

        first = results[0]
        latitude = first.get("latitude")
        longitude = first.get("longitude")
        name = first.get("name")
        country = first.get("country")
        return latitude, longitude, name, country

    def get_weather(self, latitude, longitude):
        params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
        }
        return self.api_client.safe_api_call(self.weather_url, params=params)

    def get_weather_by_city(self, city_name):
        latitude, longitude, name, country = self.get_coordinates(city_name)

        if latitude is None or longitude is None:
            return None

        display_name = f"{name}, {country}" if name and country else city_name
        print(f"📍 Found: {display_name}")
        print(f"📍 Coordinates: {latitude}, {longitude}")

        weather_data = self.get_weather(latitude, longitude)
        if weather_data:
            weather_data["_city"] = display_name
            weather_data["_coordinates"] = f"{latitude}, {longitude}"
        return weather_data

    def display_weather(self, weather_data):
        if not weather_data:
            print("❌ No weather data available.")
            return

        city = weather_data.get("_city", "Unknown")
        coordinates = weather_data.get("_coordinates", "N/A")
        current = weather_data.get("current_weather", {})

        temperature = current.get("temperature", "N/A")
        windspeed = current.get("windspeed", "N/A")
        winddirection = current.get("winddirection", "N/A")
        timezone = weather_data.get("timezone", "N/A")

        print("\n" + "=" * 55)
        print(f"🌤️ Weather in {city}")
        print("=" * 55)
        print(f"📍 Coordinates: {coordinates}")
        print("-" * 55)
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💨 Wind Speed: {windspeed} km/h")
        print(f"🧭 Wind Direction: {winddirection}°")
        print(f"🕐 Timezone: {timezone}")
        print("=" * 55)

    def run_exercise_1():
        print("\nExercise 1: Compare urllib and requests")
        print("-" * 55)
        client = WeatherClient()
        client.compare_urllib_and_requests()

    def run_exercise_2():
        print("\nExercise 2: Safe API call with error handling")
        print("-" * 55)
        safe_client = SafeAPIClient()

        valid_result = safe_client.safe_api_call(
        "https://api.open-meteo.com/v1/forecast",
        params={
        "latitude": 38.08,
        "longitude": 46.29,
        "current_weather": "true"
        }
        )
        print(valid_result)

        invalid_result = safe_client.safe_api_call("https://invalid-url-example.com")
        print(invalid_result)

    def run_city_weather_app():
        print("\nCity Weather App")
        print("-" * 55)
        app = CityWeatherApp()

        while True:
            city = input("🏙️ Enter city name (or 'exit' to quit): ").strip()

            if city.lower() in ["exit", "quit", "q"]:
                print("👋 Goodbye!")
                break

            if not city:
                print("⚠️ Please enter a city name.")
                continue

        weather_data = app.get_weather_by_city(city)
        app.display_weather(weather_data)
        print()

if __name__ == "__main__":
    CityWeatherApp.run_exercise_1()
    CityWeatherApp.run_exercise_2()
    CityWeatherApp.run_city_weather_app()
