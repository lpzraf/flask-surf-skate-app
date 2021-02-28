from flask import Flask, render_template, redirect, url_for, Blueprint
from application.models import SurfSpot, Town
import os, requests


# global func
def get_weather_results(city_id, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=imperial"
    r = requests.get(api_url)
    return r.json()


maps_bp = Blueprint(
    'maps',
    __name__,
    template_folder='templates'
)

# @app.route('/')
# def root():
#     return redirect(url_for('index'))

@maps_bp.route('/surf-map')
def surf_map():
    return render_template('surf_map.html')


@maps_bp.route('/skate-map')
def skate_map():
    return render_template('skate_map.html')


@maps_bp.route('/<string:map>/<string:town>')
def map_town(map, town):
    spots = SurfSpot.query.join(Town).filter_by(town_name=town).all()
    town_obj = Town.query.filter_by(town_name=town).first()
    weather = get_weather_results(town_obj.open_weather_town_id,
                                  os.getenv('WEATHER_API_KEY'))
    return render_template('map_town.html', map=map, town=town,
                           town_obj=town_obj, spots=spots, weather=weather)


@maps_bp.route('/<string:map>/<string:town>/<string:spot>')
def town_spot(map, town, spot):
    spot = SurfSpot.query.filter(SurfSpot.spot_name == spot).join(Town).filter_by(town_name=town).first()
    return render_template('town_spot.html', map=map, town=town, spot=spot)


@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')