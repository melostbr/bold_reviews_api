import requests

class ReviewsController:
    def all(self, app):
        uri = "https://apps.shopify.com/{}/reviews.json".format(app)
        return requests.get(uri).json()

