# from flask import Flask, render_template, request, redirect, url_for
# from flask_modus import Modus
# from dotenv import load_dotenv
# import os, requests
# from flask_sqlalchemy import SQLAlchemy

# load_dotenv()
# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CREDENTIALS')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# modus = Modus(app)


# class User(db.Model):

#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.Text)
#     last_name = db.Column(db.Text)

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# class Town(db.Model):

#     __tablename__ = 'towns'

#     id = db.Column(db.Integer, primary_key=True)
#     town_name = db.Column(db.Text)
#     town_surf_descr = db.Column(db.Text)
#     town_skate_descr = db.Column(db.Text)
#     town_descr = db.Column(db.Text)
#     open_weather_town_id = db.Column(db.Text)
#     surf_spots = db.relationship('SurfSpot', backref='town')

#     def __init__(self, town_name, town_surf_descr,
#                  town_skate_descr, town_descr, open_weather_town_id):
#         self.town_name = town_name
#         self.town_surf_descr = town_surf_descr
#         self.town_skate_descr = town_skate_descr
#         self.town_descr = town_descr
#         self.open_weather_town_id = open_weather_town_id


# class SurfSpot(db.Model):

#     __tablename__ = 'surf_spots'

#     id = db.Column(db.Integer, primary_key=True)
#     spot_name = db.Column(db.Text)
#     spot_descr = db.Column(db.Text)
#     spot_type = db.Column(db.Text)
#     ideal_size = db.Column(db.Text)
#     wave_type = db.Column(db.Text)
#     town_id = db.Column(db.Integer, db.ForeignKey('towns.id'))
#     surf_imgs = db.relationship('SurfImage', backref='surf_spot')

#     def __init__(self, spot_name, spot_descr,
#                  spot_type, ideal_size, wave_type):
#         self.spot_name = spot_name
#         self.spot_descr = spot_descr
#         self.spot_type = spot_type
#         self.ideal_size = ideal_size
#         self.wave_type = wave_type


# class SurfImage(db.Model):

#     __tablename__ = 'surf_imgs'

#     id = db.Column(db.Integer, primary_key=True)
#     img_url = db.Column(db.Text)
#     surf_spot_id = db.Column(db.Integer, db.ForeignKey('surf_spots.id'))

#     def __init__(self, img_url):
#         self.img_url = img_url


# global func
# def get_weather_results(city_id, api_key):
#     api_url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=imperial"
#     r = requests.get(api_url)
#     return r.json()


# @app.route('/')
# def home():
#     return render_template('home.html')


# @app.route('/')
# def root():
#     return redirect(url_for('index'))


# @app.route('/users', methods=['GET', 'POST'])
# def index():
#     users = User.query.all()
#     users_tuple = []
#     if len(users) % 2 != 0:
#         users = users[1:]
#     for user1, user2 in zip(users[0::2], users[1::2]):
#         users_tuple.append([user1, user2])

#     if request.method == 'POST':
#         new_user = User(request.form['first_name'], request.form['last_name'])
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('users/index.html', users=users_tuple)


# @app.route('/users/new')
# def new():
#     return render_template('users/new.html')


# @app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
# def show(id):
#     found_user = User.query.get(id)
#     if request.method == b'PATCH':
#         found_user.first_name = request.form['first_name']
#         found_user.last_name = request.form['last_name']
#         db.session.add(found_user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     if request.method == b"DELETE":
#         db.session.delete(found_user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('users/show.html', user=found_user)


# @app.route('/users/<int:id>/edit')
# def edit(id):
#     found_user = User.query.get(id)
#     return render_template('users/edit.html', user=found_user)


# @app.route('/surf-map')
# def surf_map():
#     return render_template('surf_map.html')


# @app.route('/skate-map')
# def skate_map():
#     return render_template('skate_map.html')


# @app.route('/<string:map>/<string:town>')
# def map_town(map, town):
#     spots = SurfSpot.query.join(Town).filter_by(town_name=town).all()
#     town_obj = Town.query.filter_by(town_name=town).first()
#     weather = get_weather_results(town_obj.open_weather_town_id, 
#                                   os.getenv('WEATHER_API_KEY'))
#     return render_template('map_town.html', map=map, town=town,
#                            town_obj=town_obj, spots=spots, weather=weather)


# @app.route('/<string:map>/<string:town>/<string:spot>')
# def town_spot(map, town, spot):
#     spot = SurfSpot.query.filter(SurfSpot.spot_name == spot).join(Town).filter_by(town_name=town).first()
#     return render_template('town_spot.html', map=map, town=town, spot=spot)


# @app.route('/community')
# def community():
#     return render_template('community.html')



# new
from application import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)