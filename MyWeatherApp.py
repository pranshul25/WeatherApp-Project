import tkinter as tk
from tkinter import font
import requests

HEIGHT = 470
WIDTH = 550


# functions for retrieving data from the Open Weather Map server and formatting into desired output

def get_weather(city):
    weather_key = 'c6f00f528c4c374f27895edb343ee34b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description'].upper()
        temp = weather['main']['temp']
        lon = weather['coord']['lon']
        lat = weather['coord']['lat']

        final_str = 'City: %s \nLongitude: %s \nLatitude: %s \nConditions: %s \nTemperature °C : %s' % (
        name, lon, lat, desc, temp)
    except:
        final_str = 'There was a problem retrieving weather information'

    return final_str

root = tk.Tk()
root.title('Weather App')
root.iconphoto(False, tk.PhotoImage(file='sun_icon.png'))

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='WeatherAppBg.PNG')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


upper_frame = tk.Frame(root, bg='#80c1ff', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

entry = tk.Entry(upper_frame, font=('Bookman Old Style', 12))
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Bookman Old Style', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

button = tk.Button(upper_frame, text='Get Weather', font=('Bookman Old Style', 10),
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

root.mainloop()
