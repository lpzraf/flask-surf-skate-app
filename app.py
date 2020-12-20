from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/surf-map')
def surf_map():
    return render_template('surf_map.html')


@app.route('/skate-map')
def skate_map():
    return render_template('skate_map.html')


@app.route('/<string:map>/<string:town>')
def map_town(map, town):
    # town_data = escribo el query aqui
    return render_template('map_town.html', map=map, town=town)


@app.route('/<string:map>/<string:town>/<string:spot>')
def town_spot(map, town, spot):
    # town_data = escribo el query aqui
    return render_template('town_spot.html', map=map, town=town, spot=spot)


@app.route('/community')
def community():
    return render_template('community.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)    