# Rain Reminder

## Description

The **Rain Reminder** project is a Python script designed to check the weather forecast using the OpenWeatherMap API. Its logical goal is to alert the user if rain is predicted in the upcoming hours, although the current version simply fetches and prints the raw weather data.

## Features

- **API Integration:** Connects to OpenWeatherMap's One Call API (or Forecast API).
- **Location Based:** Uses Latitude and Longitude to get precise weather data.
- **JSON Response:** Fetches and prints the API response in JSON format.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library:
  ```bash
  pip install requests
  ```
- An active API Key from [OpenWeatherMap](https://openweathermap.org/api).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/Rain_Reminder
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Configuration

In `main.py`, you can adjust the following variables:
- `api_key`: Your personal OpenWeatherMap API key.
- `lat` & `lon`: The coordinates for the location you want to check.

## Contributing

Feel free to fork this repository and extend its functionality!
- Parse the JSON data to check for specific weather condition codes (e.g., id < 700 usually means rain/snow).
- Send an SMS (via Twilio) or an email if rain is detected.
- Schedule the script to run automatically every morning.
