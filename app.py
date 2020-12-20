from flask import Flask, render_template, url_for, redirect
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


# @app.route('/surf-map/<string:town>')
# def map_town(town):
#     # town_data = escribo el query aqui
#     return render_template('map_town.html', town=town)

@app.route('/<string:map>/<string:town>')
def map_town(map, town):
    # town_data = escribo el query aqui
    return render_template('map_town.html', map=map, town=town)


if __name__ == '__main__':
    app.run(debug=True)