from tkinter import *
from tkinter import ttk
import requests

def data_get():
    # Get the selected city from the combobox
    city = city_name.get()

    # Send a request to the OpenWeatherMap API
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=d246dd5ef140e3ec8bdd616e9a0a42ef"
    ).json()

    # Update the labels with weather data
    w_label1.config(text=data["weather"][0]["main"])  # Main weather condition
    wb_label1.config(text=data["weather"][0]["description"])  # Weather description
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))  # Temperature in Celsius
    per_label1.config(text=data["main"]["pressure"])  # Pressure in hPa

win = Tk()
win.title("Roy Weather App")  # Title of the window
win.config(bg="skyblue")      # Background color of the window
win.geometry("500x550")       # Size of the window

# Main label for the app
name_label = Label(win, text="Roy Weather App", font=("Arial", 35, "bold"))
name_label.place(x=25, y=50, height=50, width=450)  # Position and size of the label

# StringVar to hold the selected city name
city_name = StringVar()

# List of Indian states and territories
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
    "Puducherry"
]

# Combobox for selecting a city
com = ttk.Combobox(win, values=list_name, font=("Arial", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Labels for weather information
w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Times New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 17))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Times New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Times New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

# Button to show weather information
show_button = Button(win, text="Show", font=("Arial", 20, "bold"), command=data_get)
show_button.place(x=200, y=190, height=50, width=100)

# Start the Tkinter main loop
win.mainloop()
