from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from dotenv import load_dotenv
import os
from user import User

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
modus = Modus(app)

users = []


def find_user(user_id):
    return [user for user in users if user.id == user_id][0]


# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/users', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_user = User(request.form['first_name'], request.form['last_name'])
        users.append(new_user)
        return redirect(url_for('index'))
    return render_template('index.html', users=users)


@app.route('/users/new')
def new():
    return render_template('new.html')


@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    found_user = find_user(id)
    if request.method == b'PATCH':
        found_user.first_name = request.form['first_name']
        found_user.last_name = request.form['last_name']
        return redirect(url_for('index'))
    if request.method == b"DELETE":
        users.remove(found_user)
        return redirect(url_for('index'))
    return render_template('show.html', user=found_user)


@app.route('/users/<int:id>/edit')
def edit(id):
    found_user = find_user(id)
    return render_template('edit.html', user=found_user)


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