# Weather-App :sunny:

> Weather application that displays the weather in a given city.
> Application deployed [here](https://weather-with-jesus.herokuapp.com/).

<p align="center">
  <img align="center" src="docs/web.png" alt="Web Image"/>
</p>

---

## Description

This weather app was made in two ways:

- a GUI using Tkinter module;
- a WebSite using Flask module.

The app communicates with the [OpenWeather](https://openweathermap.org/) API to retrieve the current weather information
in a location and display it on screen.

To use it, just type in the name of a city and click on the "Search Weather" button.

The info displayed is:

- City and Country name; :earth_africa:
- Weather description and icon; :partly_sunny:
- Temperatures (current, min and max); :fire:

---

## Project Structure

The application modules dependencies are the following:

<p align="center">
  <img align="center" src="docs/app-modules.png" alt="App-Modules"/>
</p>

Modules description:

- <code>app_services.py</code> - implementation of the logic of each of the application's functionalities

- <code>app_web_ui.py</code> - implementation of the website using Flask

- <code>app_desktop_ui.py</code> - implementation of the desktop application using Tkinter

---

## Author Info

- LinkedIn - [André Jesus](https://www.linkedin.com/in/andre-jesus-engineering)
- Twitter - [@andre_j3sus](https://twitter.com/andre_j3sus)
- Website - [André Jesus](https://sites.google.com/view/andre-jesus)