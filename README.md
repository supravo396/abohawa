ROY WEATHER APP


Roy Weather App is a simple Python GUI application that displays weather information for Indian states and territories using the OpenWeatherMap API.

FEATURES
  1. Select a city from a dropdown menu.
  2. View current weather, description, temperature (in °C), and pressure.

INSTALLATION:
   1. Clone the repository:  git clone https://github.com/your-username/roy-weather-app.git
                             cd roy-weather-app

   2.  Install dependencies: pip install requests
   3.  Run the app: python weather_app.py

USAGE:
  1. Open the app and select a city.
  2. Click "Show" to display weather data.

API KEY:
  Replace appid in the data_get function with your OpenWeatherMap API key:
    data = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=your_api_key"
    ).json()

