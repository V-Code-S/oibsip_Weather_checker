import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None
    except Exception as e:
        return None

def display_weather():
    location = entry.get()
    weather_data = get_weather(api_key, location)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {description}")
    else:
        messagebox.showerror("Error", "Unable to fetch weather data.")

def main():
    global api_key, entry, result_label

    api_key = "36827a8799240d3298073edd33e2ef7a"  

    root = tk.Tk()
    root.title("Weather App")

    label = tk.Label(root, text="Enter city or ZIP code:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
    get_weather_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
