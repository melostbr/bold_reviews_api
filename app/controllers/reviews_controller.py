import requests

class ReviewsController:
    def hello(self):
        return "Hello!"

    def hello_someone(self, name):
        return "Hello {}!".format(name)

    def all(self, app):
        uri = "https://apps.shopify.com/{}/reviews.json".format(app)
        return requests.get(uri).json()

