import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import controllers, models

@app.route("/<app>/reviews", methods=['GET'])
def reviews(app):
    return jsonify(controllers.ReviewsController().all(app))
