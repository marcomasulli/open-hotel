from flask import escape, request, render_template, flash, url_for, redirect
import requests
from .. import flask_app
from ..config import Config
from .forms import AgentForm, UserForm, HotelForm, HotelInfoForm, HotelInfoEdit
from copy import deepcopy
import json
from urllib.parse import urljoin

@flask_app.route("/")
@flask_app.route("/home")
def home():
    return render_template('home.html')

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

# Hotels

@flask_app.route("/hotels", methods=["GET"])
def view_hotels():
    try:
        hotels = requests.get(urljoin(Config.LOCAL_URL, 'hotels')).json()
    except:
        hotels = None
    return render_template('hotels.html', hotels=hotels)

@flask_app.route("/hotel/new", methods=["GET", "POST"])
def create_hotel():
    hotel_form = HotelForm(request.form)

    if request.method == 'POST':

        if hotel_form.validate_on_submit():
            new_hotel = hotel_form.data
            new_hotel.pop('csrf_token')
            # temp fix - will extend json encoder like https://stackoverflow.com/questions/52319562/django-object-of-type-decimal-is-not-json-serializable-and-convert-to-model-da/52319674
            post_hotel = requests.post(urljoin(Config.LOCAL_URL, 'hotels'), data=json.dumps(new_hotel))
            
            if post_hotel.status_code == 200:
                flash('You successfully created a new hotel!')
            else:
                flash('There was an error with your submission.')
                flash(post_hotel.text)

        else:
            print(hotel_form.errors)
            flash(str(hotel_form.errors))

        return redirect(url_for('create_hotel'))

    return render_template('formHotel.html', hotel_form=hotel_form)

# Hotel Info

@flask_app.route("/hotel/<hotel_id>/info", methods=["GET", "POST"])
def hotel_info(hotel_id):
    hotel_info_url = '/'.join([Config.LOCAL_URL, 'hotel', str(hotel_id), 'info'])
    try:
        hotel_info = requests.get(hotel_info_url).json()
        hotel_info_form = HotelInfoEdit(
            info_id=hotel_info.get('info_id'),
            hotel_id=hotel_info.get('hotel_id'),
            currency_code=hotel_info.get('currency_code'),
            currency_code_decimal_places=hotel_info.get('currency_code_decimal_places'),
            hotel_pms_system=hotel_info.get('hotel_pms_system'),
            location_category=hotel_info.get('location_category'),
            segment_category=hotel_info.get('segment_category'),
            hotel_category=hotel_info.get('hotel_category'),
            architectural_style=hotel_info.get('architectural_style'),
        )
    except:
        hotel_info = None
        hotel_info_form = HotelInfoForm()

    if request.method == 'POST':

        if hotel_info_form.validate_on_submit():
            new_hotel_info = hotel_info_form.data
            new_hotel_info['hotel_id'] = int(hotel_id)
            print(new_hotel_info)
            new_hotel_info.pop('csrf_token')
            # temp fix - will extend json encoder like https://stackoverflow.com/questions/52319562/django-object-of-type-decimal-is-not-json-serializable-and-convert-to-model-da/52319674
            if new_hotel_info.get('info_id') is not None:
                pass
            else: # if info_id is none, it is a new piece of info
                post_hotel_info = requests.post(hotel_info_url, data=json.dumps(new_hotel_info))
            
            if post_hotel_info.status_code == 200:
                flash('You successfully created new hotel information!')
            else:
                flash('There was an error with your submission.')
                flash(post_hotel_info.text)

        else:
            print(hotel_info_form.errors)
            flash(str(hotel_info_form.errors))

        return redirect(url_for('hotel_info', hotel_id=hotel_id))

    return render_template('formHotelInfo.html', hotel_info=hotel_info, hotel_info_form=hotel_info_form)


# RatePlans

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