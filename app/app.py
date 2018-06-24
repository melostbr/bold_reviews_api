import os
from flask import Flask, jsonify, request
from controllers.reviews_controller import ReviewsController


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/<app>/reviews", methods=['GET'])
def reviews(app):
    return jsonify(ReviewsController().all(app))


if __name__ == '__main__':
        app.run()
