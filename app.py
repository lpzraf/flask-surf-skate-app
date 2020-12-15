from flask import Flask, render_template, url_for, redirect
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/')
# def home():
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)