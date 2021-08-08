from flask import escape, request, render_template, flash, url_for, redirect
import requests
from .. import flask_app
from ..config import Config
from .forms import AgentForm, UserForm
from copy import deepcopy
import json
from urllib.parse import urljoin

@flask_app.route("/")
@flask_app.route("/home")
def home():
    return render_template('home.html')

@flask_app.route("/hotels", methods=["GET"])
def view_hotels():
    try:
        hotels = requests.get(urljoin(Config.LOCAL_URL, 'hotels')).json()
    except:
        hotels = None
    return render_template('hotels.html', hotels=hotels)

@flask_app.route("/rooms", methods=["GET"])
def view_rooms():
    try:
        rooms = requests.get(urljoin(Config.LOCAL_URL, 'rooms')).json()
    except:
        rooms = None
    return render_template('rooms.html', rooms=rooms)

# Agents

@flask_app.route("/agents", methods=["GET"])
def view_agents():
    try:
        agents = requests.get(urljoin(Config.LOCAL_URL, 'agents')).json()
    except:
        agents = None
    return render_template('agents.html', agents=agents)

@flask_app.route("/agent/new", methods=["GET", "POST"])
def create_agent():

    agent_form = AgentForm(request.form)

    if request.method == 'POST':

        if agent_form.validate_on_submit():
            new_agent = agent_form.data
            new_agent.pop('csrf_token')
            # temp fix - will extend son encoder like https://stackoverflow.com/questions/52319562/django-object-of-type-decimal-is-not-json-serializable-and-convert-to-model-da/52319674
            new_agent['agent_commission'] = float(new_agent.get('agent_commission'))
            new_agent['agent_discount'] = float(new_agent.get('agent_discount'))
            post_agent = requests.post(urljoin(Config.LOCAL_URL, 'agents'), data=json.dumps(new_agent))
            
            if post_agent.status_code == 200:
                flash('You successfully created a new agent!')
            else:
                flash('There was an error with your submission.')
                flash(post_agent.text)

        else:
            print(agent_form.errors)
            flash(str(agent_form.errors))

        return redirect(url_for('create_agent'))

    return render_template('formAgent.html', agent_form=agent_form)

# Users   

@flask_app.route("/users", methods=["GET"])
def view_users():
    try:
        users = requests.get(urljoin(Config.LOCAL_URL, 'users')).json()
    except:
        users = None
    return render_template('users.html', users=users)  

@flask_app.route("/user/new", methods=["GET", "POST"])
def create_user():

    user_form = UserForm(request.form)

    if request.method == 'POST':

        if user_form.validate_on_submit():
            new_user = user_form.data
            new_user.pop('csrf_token')
            # temp fix - will extend json encoder like https://stackoverflow.com/questions/52319562/django-object-of-type-decimal-is-not-json-serializable-and-convert-to-model-da/52319674
            post_user = requests.post(urljoin(Config.LOCAL_URL, 'users'), data=json.dumps(new_user))
            
            if post_user.status_code == 200:
                flash('You successfully created a new user!')
            else:
                flash('There was an error with your submission.')
                flash(post_user.text)

        else:
            print(user_form.errors)
            flash(str(user_form.errors))

        return redirect(url_for('create_user'))

    return render_template('formUser.html', user_form=user_form)

@flask_app.route("/rateplans", methods=["GET"])
def view_rateplans():
    try:
        rateplans = requests.get(urljoin(Config.LOCAL_URL, 'rateplans')).json()
    except:
        rateplans = None
    return render_template('rateplans.html', rateplans=rateplans)

@flask_app.route("/availability", methods=["GET"])
def view_availability():
    try:
        availability = requests.get(urljoin(Config.LOCAL_URL, 'availability')).json()
    except:
        availability = None
    return render_template('availability.html', availability=availability)