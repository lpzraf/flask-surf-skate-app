from flask import Flask
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from application.models import db

app = Flask(__name__)

# Using a production configuration
# app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')


bcrypt = Bcrypt(app)

db.init_app(app)
with app.app_context():
    db.create_all()

modus = Modus(app)  # for overwriting http methods

from application.users.routes import users_bp
from application.posts.routes import posts_bp
from application.auth.routes import auth_bp


app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(posts_bp, url_prefix='/users/<int:user_id>/posts')
app.register_blueprint(auth_bp)
