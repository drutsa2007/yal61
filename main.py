from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return "Привет из Лицея!"


if __name__ == '__main__':
    app.run()