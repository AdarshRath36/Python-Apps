# Python Weather App (Tkinter)

This is a desktop weather application built using Python and Tkinter.  
It allows users to search for real-time weather information of any city using the OpenWeatherMap API and displays the data in a simple, visually pleasant interface.

---

## Features

- Search weather by city name
- Displays:
  - Weather condition
  - Description
  - Temperature (°C)
  - Feels-like temperature
  - Humidity
- Dynamic weather icons based on conditions
- Keyboard support (press **Enter** to search)
- Error handling for invalid city names, API issues, and network problems
- Clean and user-friendly UI

---

## Technologies Used

- Python
- Tkinter (GUI)
- Requests (HTTP requests)
- OpenWeatherMap API

---

## Project Structure

weather-app/
├─ app.py
├─ README.md
└─ assets/
├─ icon.png
├─ sunny.png
├─ rain.png
├─ cloud.png
├─ snow.png
├─ fog.png
├─ thunder.png
├─ wind.png
├─ tornado.png
└─ volcano.png


> The `assets` folder is required.  
> Do not rename or move it, as the application loads images from this folder.

---

## How to Run the Application

### 1. Requirements
- Python 3.x
- Active internet connection (required for fetching weather data)

### 2. Install Dependencies
Open a terminal in the project folder and run:
pip install requests

### 3. Run the App

---

## Internet Requirement

This application **requires an active internet connection** because it fetches real-time weather data from the OpenWeatherMap API.

If there is:
- No internet connection  
- API server issue  

An appropriate error message will be shown.

---

## Usage

- Enter a city name in the input field
- Press **Enter** or click **Search**
- Weather details and icon will update automatically

---

## Notes

- Temperature values are converted from Kelvin to Celsius
- API key is currently hardcoded for learning purposes
- Designed mainly for educational and personal use
- Best tested on Windows systems

---

## Possible Improvements

- Add hourly or weekly forecast
- Improve UI responsiveness
- Store API key securely
- Add unit switching (°C / °F)

---

