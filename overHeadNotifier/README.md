# Overhead Notifier

## Description

The **Overhead Notifier** is a Python script designed to interact with a web API to check for specific conditions based on geographic location (Latitude and Longitude). Typically, this type of project is used to track the International Space Station (ISS) and send a notification when it is flying overhead.

*Note: The current `main.py` is a starting point and requires a valid API URL and completed logic to function fully.*

## Features

- **Location Config:** Variable settings for Latitude and Longitude.
- **API Request:** Uses the `requests` library to fetch data from an external service.
- **JSON Handling:** Parsing of JSON responses (planned).

## Prerequisites

- Python 3.x installed on your system.
- `requests` module (`pip install requests`).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/overHeadNotifier
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Contributing

Feel free to fork this repository and complete the implementation!
- Add the correct API endpoint (e.g., sending a request to `http://api.open-notify.org/iss-now.json`).
- Implement the logic to compare the ISS position with your coordinates.
- Add an email or desktop notification system.
