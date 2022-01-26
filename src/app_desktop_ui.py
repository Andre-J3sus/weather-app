from tkinter import *
import tkinter.messagebox
from src.app_services import *

# Screen configuration
app = Tk()
app.title("Weather App - by Jesus")
app.geometry("300x350")
app.resizable(False, False)
app.eval('tk::PlaceWindow . center')
bg = "sky blue"
app["bg"] = bg

# Entry to type the name of the city
city_entry = Entry(app, width=20, font=("courier", 18, "bold"), justify="center")
# Placeholder
city_entry.bind("<FocusIn>", lambda args: city_entry.delete('0', 'end'))
city_entry.insert(0, "City name")
city_entry.pack()


def search_weather():
    """
    Searches the weather.
    """
    global img, bg, weather_info_list
    city_name = city_entry.get().capitalize()
    weather_info = get_city_weather(city_name)

    if weather_info is None:  # If the search fails, a message box appears
        city_entry.delete(0, END)
        tkinter.messagebox.showwarning(title="Warning!", message="City not found! :( Try again!")

    else:
        # Update background color: purple at night; blue at day
        bg = "mediumpurple1" if weather_info[3][2] == "n" else "sky blue"
        app["bg"] = bg
        for info in weather_info_list:
            info["bg"] = bg

        # Update labels text
        location_label["text"] = f"{weather_info[city_index]}, {weather_info[1]}"
        temperature_label["text"] = f"{round(weather_info[2], 1)}°C"
        img["file"] = '../docs/weather_icons/{}.png'.format(weather_info[3])
        weather_description["text"] = weather_info[4].capitalize()
        min_max_temp_label["text"] = f"Min: {round(weather_info[5], 1)}°C\n Max: {round(weather_info[6], 1)}°C"


# Search button
search_btn = Button(app, text="Search Weather", width=16, font=("helvetica", 14, "bold"), command=search_weather)
search_btn.pack()

# Weather display
location_label = Label(app, text="City, Country", font=("helvetica", 20, "bold"), bg=bg)
location_label.pack()

img = PhotoImage(file="../docs/weather_icons/01d.png")
weather_img = Label(app, image=img, bg="sky blue")
weather_img.pack()

weather_description = Label(app, text="Description", font=("helvetica", 16, "bold"), bg=bg)
weather_description.pack()

temperature_label = Label(app, text="Temperature", font=("verdana", 16, "bold"), bg=bg)
temperature_label.pack()

min_max_temp_label = Label(app, text="Min: \n Max:", font=("verdana", 12, "bold"), bg=bg)
min_max_temp_label.pack()

weather_info_list = [location_label, weather_img, weather_description, temperature_label, min_max_temp_label]

app.mainloop()
