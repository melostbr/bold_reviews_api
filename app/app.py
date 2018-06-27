import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from controllers.reviews_controller import ReviewsController


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/<app>/reviews", methods=['GET'])
def reviews(app):
    return jsonify(ReviewsController().all(app))


if __name__ == '__main__':
        app.run()
