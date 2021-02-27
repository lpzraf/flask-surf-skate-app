from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

# association table
followers = db.Table('followers', db.Column('follower_id', db.Integer,
                     db.ForeignKey('users.id')), db.Column('followed_id',
                     db.Integer, db.ForeignKey('users.id')))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(20), unique=True)
    last_name = db.Column(db.String(20), unique=True)
    date = db.Column(db.DateTime)
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic',
        cascade="all, delete")
    # many-to-many
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __init__(self, username, password, first_name, last_name, date):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.first_name = first_name
        self.last_name = last_name
        self.date = date

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username=username).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(
                found_user.password,
                password)
            if authenticated_user:
                return found_user
        return False

    # add and remove relationships
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_notes(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.date.desc())


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime)
    post_body = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, date, post_body, user_id):
        self.title = title
        self.date = date
        self.post_body = post_body
        self.user_id = user_id


class Town(db.Model):

    __tablename__ = 'towns'

    id = db.Column(db.Integer, primary_key=True)
    town_name = db.Column(db.Text)
    town_surf_descr = db.Column(db.Text)
    town_skate_descr = db.Column(db.Text)
    town_descr = db.Column(db.Text)
    open_weather_town_id = db.Column(db.Text)
    surf_spots = db.relationship('SurfSpot', backref='town')

    def __init__(self, town_name, town_surf_descr,
                 town_skate_descr, town_descr, open_weather_town_id):
        self.town_name = town_name
        self.town_surf_descr = town_surf_descr
        self.town_skate_descr = town_skate_descr
        self.town_descr = town_descr
        self.open_weather_town_id = open_weather_town_id


class SurfSpot(db.Model):

    __tablename__ = 'surf_spots'

    id = db.Column(db.Integer, primary_key=True)
    spot_name = db.Column(db.Text)
    spot_descr = db.Column(db.Text)
    spot_type = db.Column(db.Text)
    ideal_size = db.Column(db.Text)
    wave_type = db.Column(db.Text)
    town_id = db.Column(db.Integer, db.ForeignKey('towns.id'))
    surf_imgs = db.relationship('SurfImage', backref='surf_spot')

    def __init__(self, spot_name, spot_descr,
                 spot_type, ideal_size, wave_type):
        self.spot_name = spot_name
        self.spot_descr = spot_descr
        self.spot_type = spot_type
        self.ideal_size = ideal_size
        self.wave_type = wave_type


class SurfImage(db.Model):

    __tablename__ = 'surf_imgs'

    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.Text)
    surf_spot_id = db.Column(db.Integer, db.ForeignKey('surf_spots.id'))

    def __init__(self, img_url):
        self.img_url = img_url
