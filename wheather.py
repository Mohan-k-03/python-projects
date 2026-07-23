import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    api_key = "74a6d652XXXXXXXXXXXXXX0376a2"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        city = data['name']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        # Update the UI label
        result_text = f"{city}\nTemperature: {temp}°C\nCondition: {desc.capitalize()}\nHumidity: {humidity}%"
        result_label.config(text=result_text)
        
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or invalid API key.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Python Weather App")
app.geometry("300x350")
app.configure(padx=20, pady=20)

tk.Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

search_btn = tk.Button(app, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white")
search_btn.pack(pady=15)

result_label = tk.Label(app, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=20)

app.mainloop()