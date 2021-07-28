from flask import escape, request, render_template
import requests
from .. import flask_app


@flask_app.route("/")
@flask_app.route("/home")
def home():
    return render_template('home.html')

@flask_app.route("/hotels", methods=["GET"])
def view_hotels():
    try:
        hotels = requests.get('http://localhost:8000/hotels').json()
    except:
        hotels = None
    return render_template('hotels.html', hotels=hotels)

@flask_app.route("/rooms", methods=["GET"])
def view_rooms():
    try:
        rooms = requests.get('http://localhost:8000/rooms').json()
    except:
        rooms = None
    return render_template('rooms.html', rooms=rooms)

@flask_app.route("/agents", methods=["GET"])
def view_agents():
    try:
        agents = requests.get('http://localhost:8000/agents').json()
    except:
        agents = None
    return render_template('agents.html', agents=agents)

@flask_app.route("/rateplans", methods=["GET"])
def view_rateplans():
    try:
        rateplans = requests.get('http://localhost:8000/rateplans').json()
    except:
        rateplans = None
    return render_template('rateplans.html', rateplans=rateplans)