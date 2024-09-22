from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Lead, Interaction, Task

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
