# File: main_flask.py
# A simple program that gets the name of twitter account and creates map

from flask import Flask, render_template, request
from modules.info import get_main_info

app = Flask(__name__)


@app.route("/")
def start_page():
    return render_template("index.html")


@app.route("/login")
def login():
    choice = request.args.get("nm")
    if choice == "page":
        return render_template("get_data.html")
    elif choice == "stuff":
        return render_template("wiki_sources.html")
    else:
        return "Something went wrong"


@app.route("/data")
def data():
    choice = request.args.get("name")
    if choice == "get data":
        # get_main_info(1, request.args.get("nm"), request.args.get("num"))
        info = get_main_info(1, "Claude Monet", 3)
        return str(info)
    else:
        info = get_main_info(0, choice)
        return str(info)


if __name__ == "__main__":
    app.run(debug=True)
