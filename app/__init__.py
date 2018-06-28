import os, time
from threading import Timer
from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS
app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import controllers, models

# Routes
CORS(app)
@app.route("/<app>/reviews")
def reviews(app):
    page = request.args.get('page', 1, type=int)
    return jsonify(controllers.ReviewsController().fetch_reviews(app, page))

# Scheduler
def update_reviews_schema():
    begin = datetime.now()
    controllers.ReviewsController().save_reviews()
    end = datetime.now()
    time_elapsed = end - begin
    print("Schema updated. Time elapsed:", time_elapsed.int_seconds())

def scheduler():
    Timer(1800, update_reviews_schema, ()).start()

scheduler()
