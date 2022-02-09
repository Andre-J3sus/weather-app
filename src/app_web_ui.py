from flask import Flask, request, render_template
from src.app_services import *
import os

template_dir = os.path.abspath('../templates')
static_dir = os.path.abspath('../static')
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


@app.route("/", methods=["POST", "GET"])
def home():
    """
    Shows the home page.
    """
    if request.method == "POST" and request.form["city"].strip() != "":
        city = request.form["city"]
        weather_info = get_city_weather(city)
        return render_template("base.html",
                               city=weather_info[city_index],
                               country=weather_info[country_index],
                               icon=weather_info[icon_index],
                               weather=weather_info[weather_index].capitalize(),
                               temp=weather_info[temp_index]
                               )
    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
